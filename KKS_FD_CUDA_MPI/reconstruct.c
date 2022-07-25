#include <stdio.h>
#include <stdlib.h>
#include <cuda.h>
#include <arpa/inet.h>
#include <endian.h>

#define  IS_BIG_ENDIAN     (1 == htons(1))
#define  IS_LITTLE_ENDIAN  (!IS_BIG_ENDIAN)

#include "structures.h"
#include "inputReader.c"
#include "utilityFunctions.c"

double swap_bytes(double value)
{
    double  src_num = value;
    int64_t tmp_num = htobe64(le64toh(*(int64_t*)&src_num));
    double  dst_num = *(double*)&tmp_num;
    return  dst_num;
}

void writeVTK_ASCII(double **phi, double **comp,
                    domainInfo simDomain,
                    int t, char *argv[])
{
    FILE *fp;
    char name[100];

    int layer_size = simDomain.MESH_X * simDomain.MESH_Y;

    sprintf(name, "DATA/%s_%07d.vtk", argv[2], t);
    fp = fopen(name, "w");

    /*
     * Metadata required for the reader to understand the data's topology and format
     */
    fprintf(fp, "# vtk DataFile Version 3.0\n");
    fprintf(fp, "Microsim_fields\n");
    fprintf(fp, "ASCII\n");
    fprintf(fp, "DATASET STRUCTURED_POINTS\n");
    fprintf(fp, "DIMENSIONS %d %d %d\n", simDomain.MESH_X, simDomain.MESH_Y, simDomain.MESH_Z);
    fprintf(fp, "ORIGIN 0 0 0\n");
    fprintf(fp, "SPACING %le %le %le\n", simDomain.DELTA_X, simDomain.DELTA_Y, simDomain.DELTA_Z);
    fprintf(fp, "POINT_DATA %d\n", simDomain.MESH_X*simDomain.MESH_Y*simDomain.MESH_Z);

    for (int b = 0; b < simDomain.numComponents-1; b++)
    {
        fprintf(fp, "SCALARS %s double 1\n", simDomain.componentNames[b]);
        fprintf(fp, "LOOKUP_TABLE default\n");

        for (int z = 0; z < simDomain.MESH_Z; z++)
        {
            for (int y = 0; y < simDomain.MESH_Y; y++)
            {
                for (int x = 0; x < simDomain.MESH_X; x++)
                {
                    fprintf(fp, "%le\n", comp[b][z*layer_size + y*simDomain.MESH_X + x]);
                }
            }
        }
        fprintf(fp, "\n");
    }

    for (int a = 0; a < simDomain.numPhases; a++)
    {
        fprintf(fp, "SCALARS %s double 1\n", simDomain.phaseNames[a]);
        fprintf(fp, "LOOKUP_TABLE default\n");


        for (int z = 0; z < simDomain.MESH_Z; z++)
        {
            for (int y = 0; y < simDomain.MESH_Y; y++)
            {
                for (int x = 0; x < simDomain.MESH_X; x++)
                {
                    fprintf(fp, "%le\n", phi[a][z*layer_size + y*simDomain.MESH_X + x]);
                }
            }
        }

        fprintf(fp, "\n");
    }

    fclose(fp);
}

void writeVTK_BINARY(double **phi, double **comp,
                     domainInfo simDomain,
                     int t, char *argv[])
{
    FILE *fp;
    char name[100];

    int layer_size = simDomain.MESH_X * simDomain.MESH_Y;

    double value;

    sprintf(name, "DATA/%s_%07d.vtk", argv[2], t);
    fp = fopen(name, "w");

    /*
     * Metadata required for the reader to understand the data's topology and format
     */
    fprintf(fp, "# vtk DataFile Version 3.0\n");
    fprintf(fp, "Microsim_fields\n");
    fprintf(fp, "BINARY\n");
    fprintf(fp, "DATASET STRUCTURED_POINTS\n");
    fprintf(fp, "DIMENSIONS %d %d %d\n", simDomain.MESH_X, simDomain.MESH_Y, simDomain.MESH_Z);
    fprintf(fp, "ORIGIN 0 0 0\n");
    fprintf(fp, "SPACING %le %le %le\n", simDomain.DELTA_X, simDomain.DELTA_Y, simDomain.DELTA_Z);
    fprintf(fp, "POINT_DATA %d\n", simDomain.MESH_X*simDomain.MESH_Y*simDomain.MESH_Z);

    for (int b = 0; b < simDomain.numComponents-1; b++)
    {
        fprintf(fp, "SCALARS %s double 1\n", simDomain.componentNames[b]);
        fprintf(fp, "LOOKUP_TABLE default\n");

        for (int z = 0; z < simDomain.MESH_Z; z++)
        {
            for (int y = 0; y < simDomain.MESH_Y; y++)
            {
                for (int x = 0; x < simDomain.MESH_X; x++)
                {
                    if (IS_LITTLE_ENDIAN)
                        value = swap_bytes(comp[b][z*layer_size + y*simDomain.MESH_X + x]);
                    else
                        value = comp[b][z*layer_size + y*simDomain.MESH_X + x];
                    fwrite(&value, sizeof(double), 1, fp);
                }
            }
        }
        fprintf(fp, "\n");
    }

    for (int a = 0; a < simDomain.numPhases; a++)
    {
        fprintf(fp, "SCALARS %s double 1\n", simDomain.phaseNames[a]);
        fprintf(fp, "LOOKUP_TABLE default\n");


        for (int z = 0; z < simDomain.MESH_Z; z++)
        {
            for (int y = 0; y < simDomain.MESH_Y; y++)
            {
                for (int x = 0; x < simDomain.MESH_X; x++)
                {
                    if (IS_LITTLE_ENDIAN)
                        value = swap_bytes(phi[a][z*layer_size + y*simDomain.MESH_X + x]);
                    else
                        value = phi[a][z*layer_size + y*simDomain.MESH_X + x];
                    fwrite(&value, sizeof(double), 1, fp);

                }
            }
        }

        fprintf(fp, "\n");
    }

    fclose(fp);
}

int readVTK_ASCII(FILE *fp, double **phi, double **comp,
                  domainInfo simDomain,
                  int t, int *currPos)
{
    char temp[1000];
    int a = 0, k = 0, x, y, z;
    double value;

    int temp_mx = 0, temp_my = 0, temp_mz = 0;

    int layer_size;

    while(fscanf(fp, "%s", temp))
    {
        if (strcmp(temp, "DIMENSIONS") == 0)
        {
            if(fscanf(fp, "%d", &temp_mx));
            if(fscanf(fp, "%d", &temp_my));
            if(fscanf(fp, "%d", &temp_mz));

            layer_size = temp_my*temp_mx;
            //             printf("Read dimensions: %d, %d, %d\n", temp_mx, temp_my, temp_mz);
            //             printf("Required dimensions: %d, %d, %d\n", (subdomain.xE-subdomain.xS+1), (subdomain.yE-subdomain.yS+1), (subdomain.zE-subdomain.zS+1));

        }
        else if (strcmp(temp, "SPACING") == 0)
        {
            double temp_dx = 0, temp_dy = 0, temp_dz = 0;

            if(fscanf(fp, "%le", &temp_dx));
            if(fscanf(fp, "%le", &temp_dy));
            if(fscanf(fp, "%le", &temp_dz));

        }
        else if (strcmp(temp, "default") == 0 && k < simDomain.numComponents-1)
        {
            // printf("Reading %s\n", simDomain.componentNames[k]);

            for (z = 0; z < temp_mz; z++)
            {
                for (y = 0; y < temp_my; y++)
                {
                    for (x = 0; x < temp_mx; x++)
                    {
                        if(fscanf(fp, "%le", &comp[k][*currPos + z*layer_size + y*simDomain.MESH_X + x]));
                    }
                }
            }
            k++;
        }
        else if (strcmp(temp, "default") == 0 && a < simDomain.numPhases && k >= simDomain.numComponents-1)
        {
            // printf("Reading %s\n", simDomain.phaseNames[a]);

            for (z = 0; z < temp_mz; z++)
            {
                for (y = 0; y < temp_my; y++)
                {
                    for (x = 0; x < temp_mx; x++)
                    {
                        if(fscanf(fp, "%le", &phi[a][*currPos + z*layer_size + y*simDomain.MESH_X + x]));
                    }
                }
            }
            a++;
        }
        else if (a == simDomain.numPhases)
            break;
    }

    *currPos += temp_mx*temp_my*temp_mz;

    return 1;
}

int readVTK_BINARY(FILE *fp, double **phi, double **comp,
                   domainInfo simDomain,
                   int t, int *currPos)
{
    char temp[1000];
    int a = 0, k = 0, x, y, z;
    double value;

    int temp_mx = 0, temp_my = 0, temp_mz = 0;

    int layer_size;

    while(fscanf(fp, "%s", temp))
    {
        if (strcmp(temp, "DIMENSIONS") == 0)
        {
            if(fscanf(fp, "%d", &temp_mx));
            if(fscanf(fp, "%d", &temp_my));
            if(fscanf(fp, "%d", &temp_mz));
            layer_size = temp_my*temp_mx;

            //             printf("Read dimensions: %d, %d, %d\n", temp_mx, temp_my, temp_mz);
            //             printf("Required dimensions: %d, %d, %d\n", (subdomain.xE-subdomain.xS+1), (subdomain.yE-subdomain.yS+1), (subdomain.zE-subdomain.zS+1));

        }
        else if (strcmp(temp, "SPACING") == 0)
        {
            double temp_dx = 0, temp_dy = 0, temp_dz = 0;

            if(fscanf(fp, "%le", &temp_dx));
            if(fscanf(fp, "%le", &temp_dy));
            if(fscanf(fp, "%le", &temp_dz));

        }
        else if (strcmp(temp, "default") == 0 && k < simDomain.numComponents-1)
        {
            // printf("Reading %s\n", simDomain.componentNames[k]);
            if(fscanf(fp, "%le", &value));

            for (z = 0; z < temp_mz; z++)
            {
                for (y = 0; y < temp_my; y++)
                {
                    for (x = 0; x < temp_mx; x++)
                    {
                        if(fread(&value, sizeof(double), 1, fp));
                        if (IS_LITTLE_ENDIAN)
                            comp[k][*currPos + z*layer_size + y*simDomain.MESH_X + x] = swap_bytes(value);
                        else
                            comp[k][*currPos + z*layer_size + y*simDomain.MESH_X + x] = value;

                    }
                }
            }
            k++;
        }
        else if (strcmp(temp, "default") == 0 && a < simDomain.numPhases && k >= simDomain.numComponents-1)
        {
            // printf("Reading %s\n", simDomain.phaseNames[a]);
            if(fscanf(fp, "%le", &value));

            for (z = 0; z < temp_mz; z++)
            {
                for (y = 0; y < temp_my; y++)
                {
                    for (x = 0; x < temp_mx; x++)
                    {
                        if(fread(&value, sizeof(double), 1, fp));
                        if (IS_LITTLE_ENDIAN)
                            phi[a][*currPos + z*layer_size + y*simDomain.MESH_X + x] = swap_bytes(value);
                        else
                            phi[a][*currPos + z*layer_size + y*simDomain.MESH_X + x] = value;

                    }
                }
            }
            a++;
        }
        else if (a == simDomain.numPhases)
            break;
    }

    *currPos += temp_mx*temp_my*temp_mz;

    return 1;
}

int main(int argc, char *argv[])
{

    if (argc < 6)
    {
        printf("Run as follows:\n./reconstruct.out <Name of input file> <Name of output file (must be located in DATA/Processsor_)> <Number of workers> <Start time> <End Time>\n");
        return 0;
    }

    domainInfo      simDomain;              // Global mesh size and cell size
    controls        simControls;            // Timestep, num. of iterations, etc.
    simParameters   simParams;              // All the simulation parameters and details

    // Phase-field variables
    double **phi;
    double **comp;

    FILE *fp;

    char name[1000], writeformat[10];

    // Read input from specified input file
    readInput_MPI(&simDomain, &simControls, &simParams, 0, argv);

    phi = (double**)malloc(sizeof(double*)*simDomain.numPhases);
    comp = (double**)malloc(sizeof(double*)*(simDomain.numComponents-1));

    for (int i = 0; i < simDomain.numPhases; i++)
        phi[i]  = (double*)malloc(sizeof(double)*simDomain.MESH_X*simDomain.MESH_Y*simDomain.MESH_Z);

    for (int i = 0; i < simDomain.numComponents-1; i++)
        comp[i] = (double*)malloc(sizeof(double)*simDomain.MESH_X*simDomain.MESH_Y*simDomain.MESH_Z);

    for (int t = atoi(argv[4]); t <= atoi(argv[5]); t++)
    {
        int currPos = 0;
        int i = 0;

        for (i = 0; i < atoi(argv[3]); i++)
        {
            sprintf(name, "DATA/Processor_%d/%s_%07d.vtk", i, argv[2], t);
            if (fp = fopen(name, "rb"))
            {
                if (i == atoi(argv[3])-1)
                    printf("\nReading from %s\n", name);

                if(fscanf(fp, "%*[^\n]\n"));
                if(fscanf(fp, "%*[^\n]\n"));

                if(fscanf(fp, "%s", writeformat));

                if (strcmp(writeformat, "ASCII") == 0)
                {
                    if (readVTK_ASCII(fp, phi, comp, simDomain, t, &currPos))
                    {
                        //printf("Read %s successfully\n", name);
                    }
                    else
                    {
                        printf("Verify input and saved files\n");
                        exit(-1);
                    }
                }
                else if (strcmp(writeformat, "BINARY") == 0)
                {
                    if (readVTK_BINARY(fp, phi, comp, simDomain, t, &currPos))
                    {
                        // printf("Read %s successfully\n", name);
                    }
                    else
                    {
                        printf("Verify input and saved files\n");
                        exit(-1);
                    }
                }
                fclose(fp);
            }
            else
                break;
        }

        if (strcmp(writeformat, "ASCII") == 0 && i == atoi(argv[3]))
            writeVTK_ASCII(phi, comp, simDomain, t, argv);
        else if (strcmp(writeformat, "BINARY") == 0 && i == atoi(argv[3]))
            writeVTK_BINARY(phi, comp, simDomain, t, argv);
    }

    free(phi);
    free(comp);
    freeVars(&simDomain, &simParams);

    return 0;
}
