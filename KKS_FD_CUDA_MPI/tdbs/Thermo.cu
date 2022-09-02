/******************************************************************************
 *                       Code generated with sympy 1.8                        *
 *                                                                            *
 *              See http://www.sympy.org/ for more information.               *
 *                                                                            *
 *                       This file is part of 'project'                       *
 ******************************************************************************/
#include "Thermo.cuh"
//#include <math.h>

extern __device__ __host__ void GE_0(double T, double *y, double *Ge) {

   (*Ge) = 8.3145000000000007*T*(1.0*((y[0] > 1.0000000000000001e-15) ? (
      log(y[0])*y[0]
   )
   : (
      0
   )) + 1.0*((y[1] > 1.0000000000000001e-15) ? (
      log(y[1])*y[1]
   )
   : (
      0
   )))/(1.0*y[0] + 1.0*y[1]) + (((T >= 298.0 && T < 6000.0) ? (
      -1.8*T + ((T >= 298.0 && T < 700.0) ? (
         -8.7766400000000004e-7*pow(T, 3) - 0.0018846620000000001*pow(T, 2) - 24.3672*T*log(T) + 137.07149999999999*T - 7976.1499999999996 + 74092/T
      )
      : ((T >= 700.0 && T < 933.60000000000002) ? (
         -5.7642270000000003e-6*pow(T, 3) + 0.018531981999999999*pow(T, 2) - 38.584429999999998*T*log(T) + 223.02690000000001*T - 11276.24 + 74092/T
      )
      : ((T >= 933.60000000000002 && T < 2900.0) ? (
         -31.748190000000001*T*log(T) + 188.66200000000001*T - 11277.68 - 1.23426e+28/pow(T, 9)
      )
      : (
         0
      )))) + 5481
   )
   : (
      0
   ))*y[0] + ((T >= 298.0 && T < 692.70000000000005) ? (
      -1.264963e-6*pow(T, 3) - 0.0017120340000000001*pow(T, 2) - 23.701309999999999*T*log(T) + 118.4693*T - 7285.7870000000003
   )
   : ((T >= 692.70000000000005 && T < 1700.0) ? (
      -31.379999999999999*T*log(T) + 172.3449*T - 11070.6 + 4.7065699999999997e+26/pow(T, 9)
   )
   : (
      0
   )))*y[1])/(1.0*y[0] + 1.0*y[1]) + ((18821.0 - 8.9525500000000005*T)*y[0]*y[1] - 702.79999999999995*pow(y[0] - y[1], 3)*y[0]*y[1])/(1.0*y[0] + 1.0*y[1]);

}

extern __device__ __host__ void GE_1(double T, double *y, double *Ge) {

   (*Ge) = 8.3145000000000007*T*(1.0*((y[0] > 1.0000000000000001e-15) ? (
      log(y[0])*y[0]
   )
   : (
      0
   )) + 1.0*((y[1] > 1.0000000000000001e-15) ? (
      log(y[1])*y[1]
   )
   : (
      0
   )))/(1.0*y[0] + 1.0*y[1]) + (((T >= 298.14999999999998 && T < 1700.0) ? (
      -1.56968*T + ((T >= 298.0 && T < 692.70000000000005) ? (
         -1.264963e-6*pow(T, 3) - 0.0017120340000000001*pow(T, 2) - 23.701309999999999*T*log(T) + 118.4693*T - 7285.7870000000003
      )
      : ((T >= 692.70000000000005 && T < 1700.0) ? (
         -31.379999999999999*T*log(T) + 172.3449*T - 11070.6 + 4.7065699999999997e+26/pow(T, 9)
      )
      : (
         0
      ))) + 2969.8200000000002
   )
   : (
      0
   ))*y[1] + ((T >= 298.0 && T < 700.0) ? (
      -8.7766400000000004e-7*pow(T, 3) - 0.0018846620000000001*pow(T, 2) - 24.3672*T*log(T) + 137.07149999999999*T - 7976.1499999999996 + 74092/T
   )
   : ((T >= 700.0 && T < 933.60000000000002) ? (
      -5.7642270000000003e-6*pow(T, 3) + 0.018531981999999999*pow(T, 2) - 38.584429999999998*T*log(T) + 223.02690000000001*T - 11276.24 + 74092/T
   )
   : ((T >= 933.60000000000002 && T < 2900.0) ? (
      -31.748190000000001*T*log(T) + 188.66200000000001*T - 11277.68 - 1.23426e+28/pow(T, 9)
   )
   : (
      0
   ))))*y[0])/(1.0*y[0] + 1.0*y[1]) + ((6612.8999999999996 - 4.5911*T)*(y[0] - y[1])*y[0]*y[1] + (0.47511999999999999*T + 7297.5)*y[0]*y[1] + (3.3063500000000001*T - 3097.1999999999998)*pow(y[0] - y[1], 2)*y[0]*y[1])/(1.0*y[0] + 1.0*y[1]);

}

extern __device__ __host__ void Mu_0(double T, double *y, double *Mu) {

   Mu[0] = 8.3145000000000007*T*((y[0] > 1.0000000000000001e-15) ? (
      log(y[0]) + 1
   )
   : (
      0
   ))/(1.0*y[0] + 1.0*y[1]) - 8.3145000000000007*T*((y[1] > 1.0000000000000001e-15) ? (
      log(y[1]) + 1
   )
   : (
      0
   ))/(1.0*y[0] + 1.0*y[1]) - ((18821.0 - 8.9525500000000005*T)*y[0] - 702.79999999999995*pow(y[0] - y[1], 3)*y[0] + 2108.3999999999996*pow(y[0] - y[1], 2)*y[0]*y[1])/(1.0*y[0] + 1.0*y[1]) + ((18821.0 - 8.9525500000000005*T)*y[1] - 702.79999999999995*pow(y[0] - y[1], 3)*y[1] - 2108.3999999999996*pow(y[0] - y[1], 2)*y[0]*y[1])/(1.0*y[0] + 1.0*y[1]) + ((T >= 298.0 && T < 6000.0) ? (
      -1.8*T + ((T >= 298.0 && T < 700.0) ? (
         -8.7766400000000004e-7*pow(T, 3) - 0.0018846620000000001*pow(T, 2) - 24.3672*T*log(T) + 137.07149999999999*T - 7976.1499999999996 + 74092/T
      )
      : ((T >= 700.0 && T < 933.60000000000002) ? (
         -5.7642270000000003e-6*pow(T, 3) + 0.018531981999999999*pow(T, 2) - 38.584429999999998*T*log(T) + 223.02690000000001*T - 11276.24 + 74092/T
      )
      : ((T >= 933.60000000000002 && T < 2900.0) ? (
         -31.748190000000001*T*log(T) + 188.66200000000001*T - 11277.68 - 1.23426e+28/pow(T, 9)
      )
      : (
         0
      )))) + 5481
   )
   : (
      0
   ))/(1.0*y[0] + 1.0*y[1]) - ((T >= 298.0 && T < 692.70000000000005) ? (
      -1.264963e-6*pow(T, 3) - 0.0017120340000000001*pow(T, 2) - 23.701309999999999*T*log(T) + 118.4693*T - 7285.7870000000003
   )
   : ((T >= 692.70000000000005 && T < 1700.0) ? (
      -31.379999999999999*T*log(T) + 172.3449*T - 11070.6 + 4.7065699999999997e+26/pow(T, 9)
   )
   : (
      0
   )))/(1.0*y[0] + 1.0*y[1]);

}

extern __device__ __host__ void Mu_1(double T, double *y, double *Mu) {

   Mu[0] = 8.3145000000000007*T*((y[0] > 1.0000000000000001e-15) ? (
      log(y[0]) + 1
   )
   : (
      0
   ))/(1.0*y[0] + 1.0*y[1]) - 8.3145000000000007*T*((y[1] > 1.0000000000000001e-15) ? (
      log(y[1]) + 1
   )
   : (
      0
   ))/(1.0*y[0] + 1.0*y[1]) - ((6612.8999999999996 - 4.5911*T)*(y[0] - y[1])*y[0] + (0.47511999999999999*T + 7297.5)*y[0] + (3.3063500000000001*T - 3097.1999999999998)*(-2*y[0] + 2*y[1])*y[0]*y[1] + (3.3063500000000001*T - 3097.1999999999998)*pow(y[0] - y[1], 2)*y[0] + (4.5911*T - 6612.8999999999996)*y[0]*y[1])/(1.0*y[0] + 1.0*y[1]) + ((6612.8999999999996 - 4.5911*T)*(y[0] - y[1])*y[1] + (6612.8999999999996 - 4.5911*T)*y[0]*y[1] + (0.47511999999999999*T + 7297.5)*y[1] + (3.3063500000000001*T - 3097.1999999999998)*pow(y[0] - y[1], 2)*y[1] + (3.3063500000000001*T - 3097.1999999999998)*(2*y[0] - 2*y[1])*y[0]*y[1])/(1.0*y[0] + 1.0*y[1]) - ((T >= 298.14999999999998 && T < 1700.0) ? (
      -1.56968*T + ((T >= 298.0 && T < 692.70000000000005) ? (
         -1.264963e-6*pow(T, 3) - 0.0017120340000000001*pow(T, 2) - 23.701309999999999*T*log(T) + 118.4693*T - 7285.7870000000003
      )
      : ((T >= 692.70000000000005 && T < 1700.0) ? (
         -31.379999999999999*T*log(T) + 172.3449*T - 11070.6 + 4.7065699999999997e+26/pow(T, 9)
      )
      : (
         0
      ))) + 2969.8200000000002
   )
   : (
      0
   ))/(1.0*y[0] + 1.0*y[1]) + ((T >= 298.0 && T < 700.0) ? (
      -8.7766400000000004e-7*pow(T, 3) - 0.0018846620000000001*pow(T, 2) - 24.3672*T*log(T) + 137.07149999999999*T - 7976.1499999999996 + 74092/T
   )
   : ((T >= 700.0 && T < 933.60000000000002) ? (
      -5.7642270000000003e-6*pow(T, 3) + 0.018531981999999999*pow(T, 2) - 38.584429999999998*T*log(T) + 223.02690000000001*T - 11276.24 + 74092/T
   )
   : ((T >= 933.60000000000002 && T < 2900.0) ? (
      -31.748190000000001*T*log(T) + 188.66200000000001*T - 11277.68 - 1.23426e+28/pow(T, 9)
   )
   : (
      0
   ))))/(1.0*y[0] + 1.0*y[1]);

}

extern __device__ __host__ void dmudc_0(double T, double *y, double *Dmudc) {

   Dmudc[0] = 8.3145000000000007*T*((y[0] > 1.0000000000000001e-15) ? (
      1.0/y[0]
   )
   : (
      0
   ))/(1.0*y[0] + 1.0*y[1]) + 8.3145000000000007*T*((y[1] > 1.0000000000000001e-15) ? (
      1.0/y[1]
   )
   : (
      0
   ))/(1.0*y[0] + 1.0*y[1]) + ((-4216.7999999999993*y[0] + 4216.7999999999993*y[1])*y[0]*y[1] + 4216.7999999999993*pow(y[0] - y[1], 2)*y[0])/(1.0*y[0] + 1.0*y[1]) + ((-4216.7999999999993*y[0] + 4216.7999999999993*y[1])*y[0]*y[1] - 4216.7999999999993*pow(y[0] - y[1], 2)*y[1])/(1.0*y[0] + 1.0*y[1]) - 2*(-8.9525500000000005*T - 702.79999999999995*pow(y[0] - y[1], 3) - 2108.3999999999996*pow(y[0] - y[1], 2)*y[0] + 2108.3999999999996*pow(y[0] - y[1], 2)*y[1] + (4216.7999999999993*y[0] - 4216.7999999999993*y[1])*y[0]*y[1] + 18821.0)/(1.0*y[0] + 1.0*y[1]);

}

extern __device__ __host__ void dmudc_1(double T, double *y, double *Dmudc) {

   Dmudc[0] = 8.3145000000000007*T*((y[0] > 1.0000000000000001e-15) ? (
      1.0/y[0]
   )
   : (
      0
   ))/(1.0*y[0] + 1.0*y[1]) + 8.3145000000000007*T*((y[1] > 1.0000000000000001e-15) ? (
      1.0/y[1]
   )
   : (
      0
   ))/(1.0*y[0] + 1.0*y[1]) + (2*(6612.8999999999996 - 4.5911*T)*y[1] + 2*(3.3063500000000001*T - 3097.1999999999998)*(2*y[0] - 2*y[1])*y[1] + (6.6127000000000002*T - 6194.3999999999996)*y[0]*y[1])/(1.0*y[0] + 1.0*y[1]) + (2*(3.3063500000000001*T - 3097.1999999999998)*(-2*y[0] + 2*y[1])*y[0] + 2*(4.5911*T - 6612.8999999999996)*y[0] + (6.6127000000000002*T - 6194.3999999999996)*y[0]*y[1])/(1.0*y[0] + 1.0*y[1]) - 2*(0.47511999999999999*T + (6194.3999999999996 - 6.6127000000000002*T)*y[0]*y[1] + (6612.8999999999996 - 4.5911*T)*(y[0] - y[1]) + (6612.8999999999996 - 4.5911*T)*y[0] + (3.3063500000000001*T - 3097.1999999999998)*(-2*y[0] + 2*y[1])*y[1] + (3.3063500000000001*T - 3097.1999999999998)*pow(y[0] - y[1], 2) + (3.3063500000000001*T - 3097.1999999999998)*(2*y[0] - 2*y[1])*y[0] + (4.5911*T - 6612.8999999999996)*y[1] + 7297.5)/(1.0*y[0] + 1.0*y[1]);

}
