#!usr/bin/python3
#!/bin/bash 
import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWidgets import QLineEdit
from PyQt5.QtWidgets import QLabel
from PyQt5.QtWidgets import QGridLayout
from PyQt5.QtWidgets import QDialog
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import QTableWidgetItem
from PyQt5 import QtGui
from PyQt5 import QtCore
import os
import glob
from PyQt5.QtCore import QPropertyAnimation, QParallelAnimationGroup, QPoint, QRect

validator = QtGui.QRegExpValidator(QtCore.QRegExp(r'[0-9.]+'))
validator2 = QtGui.QRegExpValidator(QtCore.QRegExp('^\d[0-9,.]+$'))
validator2e = QtGui.QRegExpValidator(QtCore.QRegExp('^\d[0-9,.e-+]+$'))
validatorName = QtGui.QRegExpValidator(QtCore.QRegExp(r'^[A-Za-z0-9_-.]*$'))
validator2fill = QtGui.QRegExpValidator(QtCore.QRegExp(r'^\d{0-9}(\,\d{0-9})?$'))


class StartScreen(QDialog):
    def __init__(self):
        super(StartScreen,self).__init__()
        loadUi("resources/maincsreen.ui",self)
        self.setWindowTitle("NSM - MLab")
        self.logo.setStyleSheet("background-image : url(resources/MicroSim2.png)")
        self.logo_2.setStyleSheet("background-image : url(resources/MicroSim2.png)")
        self.sideBtn1.setIcon(QtGui.QIcon('resources/favicon.png'))
        self.sideBtn2.setIcon(QtGui.QIcon('resources/phases.png'))
        self.sideBtn3.setIcon(QtGui.QIcon('resources/time.png'))
        self.sideBtn4.setIcon(QtGui.QIcon('resources/nacl.png'))
        self.sideBtn5.setIcon(QtGui.QIcon('resources/shape.png'))
        self.sideBtn6.setIcon(QtGui.QIcon('resources/domain.png'))
        self.sideBtn7.setIcon(QtGui.QIcon('resources/pngegg.png'))
        self.sideInfileBtn.setIcon(QtGui.QIcon('resources/previous.png'))

        QtWidgets.QShortcut(QtGui.QKeySequence("Escape"), self, activated=self.on_Escape)

        #RESTRICTING STRING INPUT
        self.mesh_x.setValidator(validator)
        self.mesh_y.setValidator(validator)
        self.mesh_z.setValidator(validator)
        self.dx.setValidator(validator)
        self.dy.setValidator(validator)
        self.dz.setValidator(validator)
        self.dt.setValidator(validator2e)
        self.timeSteps.setValidator(validator)
        self.saveAt.setValidator(validator)
        self.Nsmooth.setValidator(validator)
        self.startTime.setValidator(validator)
        self.numWorkers.setValidator(validator)
        self.R_Value.setValidator(validator2e)
        self.V_Value.setValidator(validator2e)
        self.BC_1.setValidator(validator)
        self.BC_2.setValidator(validator)
        self.BC_3.setValidator(validator)
        self.BC_4.setValidator(validator)
        self.diffInput.setValidator(validator2e)
        self.Estrain.setValidator(validator2)
        self.Econstant.setValidator(validator2)
        self.gammaInput.setValidator(validator2e)

        #for DomainFilling

        self.cube_end.setValidator(validator2)
        self.cube_start.setValidator(validator2)
        self.cylinder_center.setValidator(validator2)
        self.cylinder_radius.setValidator(validator)
        self.cylinder_zend.setValidator(validator)
        self.cylinder_zstart.setValidator(validator)
        self.ellipse_center.setValidator(validator2)
        self.ellipse_eccentric.setValidator(validator)
        self.ellipse_majorAxis.setValidator(validator)
        self.ellipse_rotation.setValidator(validator)
        self.sphere_center.setValidator(validator2)
        self.sphere_radius.setValidator(validator)


        ##GP Validator
        self.trackProgressGP.setValidator(validator)
        self.epsilonGP.setValidator(validator)
        self.tauGP.setValidator(validator)
        self.FanisotropyGP.setValidator(validator)
        self.anisotropyTypeGP.setValidator(validator)
        self.funcWGP.setValidator(validator)
        self.funcFGP.setValidator(validator)
        self.shiftJGP.setValidator(validator)
        self.equTGP.setValidator(validator)
        self.fillingTGP.setValidator(validator)
        self.TGP.setValidator(validator)
        self.ampNoiseGP.setValidator(validator)
        self.writecompGP.setValidator(validator)


        self.TauGP.setValidator(validator2)
        self.debGP.setValidator(validator2)
        self.gammaABCGP.setValidator(validator2)
        self.tempgradyGP.setValidator(validator2)


        #CH Validator
        self.trackProgressCH.setValidator(validator)

        self.lPhiCH.setValidator(validator2)
        self.kappaPhiCH.setValidator(validator2)
        self.kappaCCH.setValidator(validator2)
        self.afmCH.setValidator(validator2)
        self.bfpCH.setValidator(validator2)

        self.infile.setValidator(validatorName)
        self.filling.setValidator(validatorName)
        self.output.setValidator(validatorName)

        #hinding Widget and Frames
        self.frame_2.hide()
        self.pwidget.hide()
        self.pwidget_2.hide()
        self.Second_widget.hide()
        self.Third_widget.hide()
        self.Four_widget.hide()
        self.Fifth_widget.hide()
        self.Sixth_widget.hide()
        self.Seven_widget.hide()
        self.shapeUpdate.hide()
        self.w1.hide()
        self.paraviewError.hide()



        #start ScreenFrame
        self.openFile.clicked.connect(self.openFileDir)
        self.startNew.clicked.connect(self.startNewClicked)
        self.importFile.clicked.connect(self.importFileClicked)
        self.close_btn.clicked.connect(self.close_btnClicked)
        self.sideInfileBtn.clicked.connect(self.sideInfileBtnClicked)


        #shape frame
        self.shapeframe.hide()
    
        #Btn click action
        self.btn1.clicked.connect(self.clickedBtn1)
        self.sideBtn1.clicked.connect(self.clickedBtn1)
        self.btn2.clicked.connect(self.clickedBtn2)


        self.next1.clicked.connect(self.NextBtn1)
        self.sideBtn2.clicked.connect(self.NextBtn1)


        self.next2.clicked.connect(self.NextBtn2)
        self.sideBtn3.clicked.connect(self.NextBtn2)


        self.next3.clicked.connect(self.NextBtn3)
        self.sideBtn4.clicked.connect(self.NextBtn3)

        self.btn3.clicked.connect(self.clickedBtn3)
        self.btn4.clicked.connect(self.clickedBtn4)

        self.next4.clicked.connect(self.NextBtn4)
        self.sideBtn5.clicked.connect(self.NextBtn4)

        self.next5.clicked.connect(self.NextBtn5)
        self.sideBtn6.clicked.connect(self.NextBtn5)

        self.next6.clicked.connect(self.NextBtn6)
        self.sideBtn7.clicked.connect(self.NextBtn6)

        self.btn5.clicked.connect(self.clickedBtn5)
        self.next7.clicked.connect(self.clickedBtn6)
        self.btn6.clicked.connect(self.clickedBtn6)
        self.btn7.clicked.connect(self.clickedBtn7)


        #action on mesh change4
        self.mesh_x.textChanged.connect(self.drawMesh)

        #action on mesh change
        self.mesh_y.textChanged.connect(self.drawMesh)

        #action on mesh change
        self.dx.textChanged.connect(self.draw_dx)

        #action on mesh change
        self.dy.textChanged.connect(self.draw_dy)
  

        #Changing Phases
        self.phasebtn.clicked.connect(self.phaseBtnClicked)
        self.phasesavebtn.clicked.connect(self.phaseSaveBtnClicked)

        #Changing Components
        self.componentbtn.clicked.connect(self.componentBtnClicked)
        self.comsavebtn.clicked.connect(self.componentSaveBtnClicked)

        self.GP_next.clicked.connect(self.GPnextClicked)
        self.GP_pre.clicked.connect(self.GPpreClicked)
        self.saveGP.clicked.connect(self.saveGPClicked)
        self.saveGP.hide()

        self.KKS_next.clicked.connect(self.KKSnextClicked)
        self.KKS_pre.clicked.connect(self.KKSpreClicked)
        self.saveKKS.clicked.connect(self.saveKKSClicked)
        self.saveKKS.hide()

        self.KKS2_next.clicked.connect(self.KKS2nextClicked)
        self.KKS2_pre.clicked.connect(self.KKS2preClicked)
        self.saveKKS2.clicked.connect(self.saveKKS2Clicked)
        self.saveKKS2.hide()

        self.CH_next.clicked.connect(self.CHnextClicked)
        self.CH_pre.clicked.connect(self.CHpreClicked)
        self.saveCH.clicked.connect(self.saveCHClicked)

        self.tableWidgetCHA.itemClicked.connect(self.tableItemClickedCHA)
        self.saveCH.hide()

        self.finish.clicked.connect(self.clickedfinish)
        self.runBtn.clicked.connect(self.clickedrunBtn)
        self.preview.clicked.connect(self.clickedpreview)
        self.paraviewErrorClose.clicked.connect(self.paraviewErrorCloseClicked)
        self.paraviewCancel.clicked.connect(self.paraviewErrorCloseClicked)
        self.paraviewBrowse.clicked.connect(self.paraviewBrowseClicked)
        self.paraviewOpen.clicked.connect(self.paraviewOpenClicked)

        #Boundary Conditions
        self.BCV_1.cursorPositionChanged.connect(self.BCV1fill)
        self.BCV_2.cursorPositionChanged.connect(self.BCV2fill)
        self.BCV_3.cursorPositionChanged.connect(self.BCV3fill)
        self.BCV_4.cursorPositionChanged.connect(self.BCV4fill)

        #shadow
        shadow = QtWidgets.QGraphicsDropShadowEffect(self,
                                                     blurRadius=10.0,
                                                     color=QtGui.QColor (63, 63, 63, 180),
                                                     offset=QtCore.QPointF(3.0, 3.0)
                                                     )
        self.frame_1.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(self,blurRadius=10.0,color=QtGui.QColor (63, 63, 63, 180),offset=QtCore.QPointF(3.0, 3.0)))
        self.frame_2.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(self,blurRadius=10.0,color=QtGui.QColor (63, 63, 63, 180),offset=QtCore.QPointF(3.0, 3.0)))
        self.frame_3.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(self,blurRadius=10.0,color=QtGui.QColor (63, 63, 63, 180),offset=QtCore.QPointF(3.0, 3.0)))
        self.frame_4.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(self,blurRadius=10.0,color=QtGui.QColor (63, 63, 63, 180),offset=QtCore.QPointF(3.0, 3.0)))
        self.frame_5.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(self,blurRadius=10.0,color=QtGui.QColor (63, 63, 63, 180),offset=QtCore.QPointF(3.0, 3.0)))
        self.frame_6.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(self,blurRadius=10.0,color=QtGui.QColor (63, 63, 63, 180),offset=QtCore.QPointF(3.0, 3.0)))
        self.frame_7.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(self,blurRadius=10.0,color=QtGui.QColor (63, 63, 63, 180),offset=QtCore.QPointF(3.0, 3.0)))
        self.frame_8.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(self,blurRadius=10.0,color=QtGui.QColor (63, 63, 63, 180),offset=QtCore.QPointF(3.0, 3.0)))
        self.frame_9.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(self,blurRadius=10.0,color=QtGui.QColor (63, 63, 63, 180),offset=QtCore.QPointF(3.0, 3.0)))
        self.frame_10.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(self,blurRadius=10.0,color=QtGui.QColor (63, 63, 63, 180),offset=QtCore.QPointF(3.0, 3.0)))
        self.frame_11.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(self,blurRadius=10.0,color=QtGui.QColor (63, 63, 63, 180),offset=QtCore.QPointF(3.0, 3.0)))
        self.ShapeList.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(self,blurRadius=10.0,color=QtGui.QColor (63, 63, 63, 180),offset=QtCore.QPointF(3.0, 3.0)))
        self.shapeframe.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(self,blurRadius=10.0,color=QtGui.QColor (63, 63, 63, 180),offset=QtCore.QPointF(3.0, 3.0)))
        self.startNew.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(self,blurRadius=10.0,color=QtGui.QColor (63, 63, 63, 180),offset=QtCore.QPointF(3.0, 3.0)))
        self.importFile.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(self,blurRadius=10.0,color=QtGui.QColor (63, 63, 63, 180),offset=QtCore.QPointF(3.0, 3.0)))
        self.w1.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(self,blurRadius=14.0,color=QtGui.QColor (63, 63, 63, 180),offset=QtCore.QPointF(4.0, 3.0)))
        self.paraviewError.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(self,blurRadius=14.0,color=QtGui.QColor (63, 63, 63, 180),offset=QtCore.QPointF(4.0, 3.0)))
        self.pwidget.setGraphicsEffect(shadow)
        self.pwidget_2.setGraphicsEffect(shadow)
        self.Qbox.setGraphicsEffect(QtWidgets.QGraphicsDropShadowEffect(self,blurRadius=10.0,color=QtGui.QColor (76,35,45, 180),offset=QtCore.QPointF(2.0, -2.0)))

        #Animations
        #self.anim1 = QPropertyAnimation(self.StartFrame, b"pos")
        #self.anim1.setEndValue(QPoint(0, 600))
        #self.anim1.setDuration(400)

        #self.anim2 = QPropertyAnimation(self.w1, b"geometry")
        #self.anim2.setEndValue(QRect(240, 150, 530, 300))
        #self.anim2.setDuration(200)

        self.anim12 = QPropertyAnimation(self.w1, b"pos")
        self.anim12.setStartValue(QPoint(230, 140))
        self.anim12.setEndValue(QPoint(230,160))
        self.anim12.setDuration(300)

        
        #VALUE CHANGE ACTION
        self.dim.valueChanged.connect(self.updateDim)
        self.Qbox.hide()
        self.reStart.valueChanged.connect(self.reStartFun)

        self.noP.valueChanged.connect(self.updateNoP)
        self.noP.lineEdit().setReadOnly(True)
        self.noC.valueChanged.connect(self.updateNoC)
        self.shiftGP.valueChanged.connect(self.updateshiftGP)
        self.tdbflagCH.valueChanged.connect(self.updatetdbflag)

        self.noiseGP.valueChanged.connect(self.updatenoiseGPflag)
        self.noiseKKS.valueChanged.connect(self.updatenoiseKKSflag)
        self.noiseKKS2.valueChanged.connect(self.updatenoiseKKS2flag)


        self.diffInput.textChanged.connect(self.FillDiffMat)
        self.gammaInput.textChanged.connect(self.FillGammaMat)
        self.pDropdown.currentIndexChanged.connect(self.phaseChange)
        self.pDropdown_2.currentIndexChanged.connect(self.phaseChange_BC)

        #for boundary condition
        self.BC_1.highlighted.connect(self.BCV1fill)
        self.BC_2.highlighted.connect(self.BCV2fill)
        self.BC_3.highlighted.connect(self.BCV3fill)
        self.BC_4.highlighted.connect(self.BCV4fill)


        self.BC_1.currentIndexChanged.connect(self.BCV1Change)
        self.BC_2.currentIndexChanged.connect(self.BCV2Change)
        self.BC_3.currentIndexChanged.connect(self.BCV3Change)
        self.BC_4.currentIndexChanged.connect(self.BCV4Change)

        self.BC_1.model().item(0).setEnabled(False)
        self.BC_1.model().item(2).setEnabled(False)
        self.BC_1.model().item(4).setEnabled(False)

        self.BC_2.model().item(0).setEnabled(False)
        self.BC_2.model().item(2).setEnabled(False)
        self.BC_2.model().item(4).setEnabled(False)

        self.BC_3.model().item(0).setEnabled(False)
        self.BC_3.model().item(2).setEnabled(False)
        self.BC_3.model().item(4).setEnabled(False)

        self.BC_4.model().item(0).setEnabled(False)
        self.BC_4.model().item(2).setEnabled(False)
        self.BC_4.model().item(4).setEnabled(False)
        self.startTime.setEnabled(False) ## ReStart Parameter

        self.allCheck_2.hide()

        #DOmain Filling
        self.shape.currentIndexChanged.connect(self.domainShapeChange)
        self.pDropdown_3.currentIndexChanged.connect(self.domainPhaseChange)
        self.addShape.clicked.connect(self.shapeframeToggle)
        self.shapeCancel.clicked.connect(self.shapeCancelClicked)
        self.shapeframeclose.clicked.connect(self.shapeCancelClicked)
        self.shapeSave.clicked.connect(self.shapeSaveClicked)
        self.shapeUpdate.clicked.connect(self.shapeUpdateClicked)
        self.shapeedit.clicked.connect(self.shapeeditClicked)
        self.shapedelete.clicked.connect(self.shapedeleteClicked)
        self.addShapeFile.clicked.connect(self.addShapeFileClicked)


        self.cubeIcon.setPixmap(QtGui.QPixmap("resources/cube.JPG"))
        self.cylinderIcon.setPixmap(QtGui.QPixmap("resources/cylinder.JPG"))
        self.ellipseIcon.setPixmap(QtGui.QPixmap("resources/ellipse.png"))
        self.sphereIcon.setPixmap(QtGui.QPixmap("resources/sphere.png"))
        self.ashokchakra.setPixmap(QtGui.QPixmap("resources/ashokchakra.png"))
        self.background.setPixmap(QtGui.QPixmap("resources/back.png"))
        self.background2.setPixmap(QtGui.QPixmap("resources/back2.png"))

        #radio toggled
        self.diffR.toggled.connect(self.fMatrixToggled)
        self.diffR_2.toggled.connect(self.dMatrixToggled)
        self.allCheck.toggled.connect(self.allCheckFunc)

        self.radio_GP.toggled.connect(self.radio_GPToggled)
        self.radio_CH.toggled.connect(self.radio_CHToggled)
        self.radio_KKR.toggled.connect(self.radio_KKRToggled)
        self.radio_KKS2.toggled.connect(self.radio_KKS2Toggled)
        self.thermalYGP.toggled.connect(self.radio_thermalYGPToggled)
        self.thermalNGP.toggled.connect(self.radio_thermalNGPToggled)
        self.thermalYKKS2.toggled.connect(self.radio_thermalYKKS2Toggled)
        self.thermalNKKS2.toggled.connect(self.radio_thermalNKKS2Toggled)


        self.es.clicked.connect(self.esToggled)
        self.es_2.clicked.connect(self.es2Toggled)
        self.es_3.clicked.connect(self.es3Toggled)

        self.allCheck_2.toggled.connect(self.allCheckBC)
        self.allCheck_BC.toggled.connect(self.allCheckBCV)


        #important Initializations
        grid = QGridLayout()
        self.diffMat.setLayout(grid)

        self.Diffusivity = []
        self.DiffusivityType = []
        self.eigenStrain = []
        self.elasticConstant = []
        self.elasticType = []

        self.Bcnd = [""]*4
        self.BconV = [""]*4
        self.ShapeFlag = 0

        self.domainType = []
        self.domainValue =[]

        if self.noP.value() == 1:
            self.pDropdown.addItem("alpha")
            self.Diffusivity.append("")
            self.DiffusivityType.append("")
            self.eigenStrain.append("")
            self.elasticConstant.append("")
            self.elasticType.append("")

            self.pDropdown_3.addItem("alpha")
            self.domainType.append("")
            self.domainValue.append("")


        header = self.tableWidgetGP.horizontalHeader()
        header.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        header.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)

        headerKKS = self.tableWidgetKKS.horizontalHeader()
        headerKKS.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        headerKKS.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)

        headerKKS2 = self.tableWidgetKKS2.horizontalHeader()
        headerKKS2.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        headerKKS2.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)

        headerCH = self.tableWidgetCH.horizontalHeader()
        headerCH.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        headerCH.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)

        headerCHA = self.tableWidgetCHA.horizontalHeader()
        headerCHA.setSectionResizeMode(0, QtWidgets.QHeaderView.ResizeToContents)
        headerCHA.setSectionResizeMode(1, QtWidgets.QHeaderView.ResizeToContents)


    @QtCore.pyqtSlot()
    def on_Escape(self):
        return

    def importFileClicked(self):
        self.w1.show()
        self.anim12.start()

    def close_btnClicked(self):
        self.w1.hide()

    def sideInfileBtnClicked(self):
        self.StartFrame.show()
        self.w1.hide()

    def resetAll(self):
        return


    def addShapeFileClicked(self):
        self.ShapefileDir, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Single File', QtCore.QDir.currentPath() )
        try:
                shapeFileDir = open(self.ShapefileDir, 'r')
                ShapeLines = shapeFileDir.readlines()
                self.StartFrame.hide()
                self.ShapeFlag = 1

                for i in ShapeLines:

                    if "#" in i:
                        pass

                    elif "=" in i and "FILL" in i:
                        i = i.replace(" ","")
                        i = i.replace(";","")
                        i = i.replace("="," ")
                        i = i.replace("\n","")
                        i = i.replace("FILL","")
                        self.ShapeList.addItem(i)

        except IOError:
            print("could not read")

        except UnicodeDecodeError:
            print("could not read")
        


    def openFileDir(self):
        if self.model_GP.isChecked() or self.model_CH.isChecked() or self.model_KKS.isChecked() or self.model_KKS2.isChecked() :
            self.errorStartScreen.setText("")
            self.fileNameDir, _ = QtWidgets.QFileDialog.getOpenFileName(self, 'Single File', QtCore.QDir.currentPath() )
            self.fileLabel.setText(self.fileNameDir)
            self.ReadfromFile()
        else:
            self.errorStartScreen.setText("Please selct the Model")
            return


    def drawMesh(self):

        if self.mesh_x.text() !="":
            self.Qbox.setGeometry(340,340,180,4)
            self.Qbox.show()
            self.error1.setText("")
        else:
            self.Qbox.hide()

        if self.mesh_y.text() !="" and self.mesh_x.text() !="":

            try:
                x_dim = float(self.mesh_x.text())
                self.error1.setText("")

            except ValueError:
                self.error1.setText("Please enter valid Mesh X")
                return

            try:
                y_dim = float(self.mesh_y.text())
                self.error1.setText("")

            except ValueError:
                self.error1.setText("Please enter valid Mesh Y")
                return

            if x_dim > y_dim:
                self.Qbox.setGeometry(340,360 - round((y_dim/x_dim)*90),180,round((y_dim/x_dim)*180))
            elif x_dim < y_dim:
                self.Qbox.setGeometry(450 - round((x_dim/y_dim)*90) ,260,  round((x_dim/y_dim)*180),180)
            else:
                self.Qbox.setGeometry(340,260,180,180)

            self.Qbox.show()

        if self.dx.text() !="" and self.dy.text() !="":
            self.draw_dx()
            self.draw_dy()


    def draw_dx(self):
        v = [self.v_0,self.v_1,self.v_2,self.v_3,self.v_4,self.v_5,self.v_6,self.v_7,self.v_8,self.v_9]
        if self.dx.text() !="" and float(self.dx.text()) > 0:

            Qwidth = self.Qbox.frameGeometry().width()
            Qheight = self.Qbox.frameGeometry().height()
            for i in range(9):
                v[i].setGeometry(round((Qwidth/10)*(i+1)),1,1,Qheight-1)

        else:
            for i in range(9):
                v[i].setGeometry(0,0,0,0)


    def draw_dy(self):
        h = [self.h_0,self.h_1,self.h_2,self.h_3,self.h_4,self.h_5,self.h_6,self.h_7,self.h_8,self.h_9,self.h_10,self.h_11,self.h_12,self.h_13,self.h_14,self.h_15,self.h_16,self.h_17,self.h_18,self.h_19,self.h_20,self.h_21,self.h_22,self.h_23,self.h_24,self.h_25,self.h_26,self.h_27,self.h_28,self.h_29,self.h_30,self.h_31,self.h_32,self.h_33,self.h_34,self.h_35,self.h_36,self.h_37,self.h_38,self.h_39,self.h_40,self.h_41,self.h_42,self.h_43,self.h_44,self.h_45,self.h_46,self.h_47,self.h_48,self.h_49,self.h_50]
        for i in range(51):
            h[i].setGeometry(0,0,0,0)

        #error Handling
        try:
            dx_value = float(self.dx.text())
            self.error2.setText("")

        except ValueError:
            self.error2.setText("dx : Value Error ")
            return

        try:
            dy_value = float(self.dy.text())
            self.error2.setText("")

        except ValueError:
            self.error2.setText("dy : Value Error ")
            return

        if dx_value == 0:
            self.error2.setText("dx cannot be equal to 0")
            return
        if dy_value == 0:
            self.error2.setText("dy cannot be equal to 0")
            return

        if self.dy.text() !="" and float(self.dy.text()) > 0:

            Qwidth = self.Qbox.frameGeometry().width()
            Qheight = self.Qbox.frameGeometry().height()

            dy_dx = dy_value/dx_value
            no_hl = round((dy_dx)*(Qwidth/10))

            if  dy_dx> 2 or dy_dx < 0.5:
                no_hl = 2*(Qwidth/10)

            try:
                num_lines = round(Qheight/no_hl)
            except ZeroDivisionError:
                return

            if len(h) < num_lines:
                num_lines = len(h)
                no_hl = 2*(Qwidth/10)
                
            for i in range(num_lines):
                h[i].setGeometry(1 , round(no_hl*(i+1)), Qwidth-1 , 1  )

        return

## All Value Change Function (Flags)
    def updateDim(self):
        if(self.dim.value() == 2):
            self.mesh_z.setText("1")
            self.mesh_z.setEnabled(False)
        else:
            self.mesh_z.setEnabled(True)

    def reStartFun(self):
        if(self.reStart.value() == 1):
            self.startTime.setEnabled(True)
        elif(self.reStart.value() == 0):
            self.startTime.setEnabled(False)

    def updateshiftGP(self):
        if(self.shiftGP.value() == 1):
            self.shiftJGP.setEnabled(True)
        elif(self.shiftGP.value() == 0):
            self.shiftJGP.setEnabled(False)

    def radio_thermalYGPToggled(self):
        if self.thermalYGP.isChecked():
            self.tempgradyGP.setEnabled(False)
        else:
            self.tempgradyGP.setEnabled(True)


    def radio_thermalNGPToggled(self):
        if self.thermalNGP.isChecked():
            self.tempgradyGP.setEnabled(True)
        else:
            self.tempgradyGP.setEnabled(False)

    def radio_thermalYKKS2Toggled(self):
        if self.thermalYKKS2.isChecked():
            self.tempGradyKKS2.setEnabled(False)
        else:
            self.tempGradyKKS2.setEnabled(True)


    def radio_thermalNKKS2Toggled(self):
        if self.thermalNKKS2.isChecked():
            self.tempGradyKKS2.setEnabled(True)
        else:
            self.tempGradyKKS2.setEnabled(False)

#Noise Flag
    def updatenoiseGPflag(self):
        if self.noiseGP.value() == 0:
            self.ampNoiseGP.setEnabled(False)

        elif self.noiseGP.value() == 1:
            self.ampNoiseGP.setEnabled(True)

    def updatenoiseKKSflag(self):
        if self.noiseKKS.value() == 0:
            self.ampNoiseKKS.setEnabled(False)

        elif self.noiseKKS.value() == 1:
            self.ampNoiseKKS.setEnabled(True)

    def updatenoiseKKS2flag(self):
        if self.noiseKKS2.value() == 0:
            self.ampNoiseKKS2.setEnabled(False)

        elif self.noiseKKS2.value() == 1:
            self.ampNoiseKKS2.setEnabled(True)


    def phaseBtnClicked(self):
        self.pwidget.show()
        self.next2.setEnabled(False)
        self.componentbtn.setEnabled(False)
        self.phasebtn.setEnabled(False)


    def phaseSaveBtnClicked(self):

        Pnames = self.ptext.toPlainText().splitlines()

        if len(Pnames) != self.noP.value():
            self.perror.setText( str(self.noP.value()) + " phase names required" )
        else:
            for i in range(len(Pnames)):
                self.pDropdown.setItemText(i,Pnames[i])
                self.pDropdown_3.setItemText(i,Pnames[i])

            self.pwidget.hide()
            self.next2.setEnabled(True)
            self.componentbtn.setEnabled(True)
            self.phasebtn.setEnabled(True)
            self.perror.setText("")


    def updateNoP(self):
        noP_value = self.noP.value()
        if(noP_value == 2):
            self.ptext.setPlainText("alpha\nbeta")


        elif (noP_value == 3):
            self.ptext.setPlainText("alpha\nbeta\ngamma")


        elif(noP_value == 1):
            self.ptext.setPlainText("alpha")


        elif (noP_value > 3 ):
            Pnames = self.ptext.toPlainText().splitlines()

            if len(Pnames) < noP_value :
                Phase_text2 = self.ptext.toPlainText()

                for i in range(noP_value - len(Pnames) ):
                    Phase_text2 = Phase_text2 +"\nP" +str(len(Pnames)+1+i)

                self.ptext.setPlainText(Phase_text2)

            if len(Pnames) > noP_value:
                Phase_text2 = Pnames[0]
                for i in range(1,noP_value,1):
                    Phase_text2 = Phase_text2 + "\n" + Pnames[i]

                self.ptext.setPlainText(Phase_text2)

        #function start
        Pnames = self.ptext.toPlainText().splitlines()
        Ndropdown = self.pDropdown.count()

        if Ndropdown < noP_value:
            for i in range(noP_value - Ndropdown):
                self.pDropdown.addItem(Pnames[Ndropdown +i])
                self.Diffusivity.append("")
                self.DiffusivityType.append("")
                self.eigenStrain.append("")
                self.elasticConstant.append("")
                self.elasticType.append("")

                self.pDropdown_3.addItem(Pnames[Ndropdown +i])
                self.domainType.append("")
                self.domainValue.append("")

        elif Ndropdown > noP_value:
            for i in range(Ndropdown - noP_value):
                self.pDropdown.removeItem(self.pDropdown.count() -1)
                self.Diffusivity.pop()
                self.DiffusivityType.pop()
                self.eigenStrain.pop()
                self.elasticConstant.pop()
                self.elasticType.pop()

                self.pDropdown_3.removeItem(self.pDropdown_3.count() -1)
                self.domainType.pop()
                self.domainValue.pop()

        #GP model
        self.tableWidgetGP.setRowCount(noP_value**2)
        self.tableWidgetGPA.setRowCount(noP_value)

        self.tableWidgetKKS.setRowCount(noP_value**2)
        self.tableWidgetKKS2.setRowCount(noP_value**2)
        self.tableWidgetKKSF.setRowCount(noP_value)

        self.tableWidgetCH.setRowCount(noP_value**2)
        self.tableWidgetCHA.setRowCount(noP_value)
        self.tableWidgetGP.setItem((noP_value*noP_value)-1,4, QTableWidgetItem(str("-")))  ## filling last column os slope

        rcount =0

        for i in range(noP_value):

            self.tableWidgetGPA.setItem(i,0, QTableWidgetItem(str(i)))
            self.tableWidgetGPA.item(i,0).setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidgetGPA.item(i,0).setFlags(self.tableWidgetGPA.item(i,0).flags() & ~QtCore.Qt.ItemIsEditable)

            self.tableWidgetKKSF.setItem(i,0, QTableWidgetItem(str(i)))
            self.tableWidgetKKSF.item(i,0).setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidgetKKSF.item(i,0).setFlags(self.tableWidgetKKSF.item(i,0).flags() & ~QtCore.Qt.ItemIsEditable)

            self.tableWidgetCHA.setItem(i,0, QTableWidgetItem(str(i)))
            self.tableWidgetCHA.item(i,0).setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidgetCHA.item(i,0).setFlags(self.tableWidgetKKSF.item(i,0).flags() & ~QtCore.Qt.ItemIsEditable)

            self.tableWidgetCHA.setItem(i,1, QTableWidgetItem(str("DM")))
            self.tableWidgetCHA.item(i,1).setTextAlignment(QtCore.Qt.AlignCenter)
            self.tableWidgetCHA.item(i,1).setFlags(self.tableWidgetKKSF.item(i,0).flags() & ~QtCore.Qt.ItemIsEditable)



            for j in range(noP_value):
                #GP
                self.tableWidgetGP.setItem(rcount,0, QTableWidgetItem(str(i)))
                self.tableWidgetGP.setItem(rcount,1, QTableWidgetItem(str(j)))
                self.tableWidgetGP.item(rcount,0).setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidgetGP.item(rcount,1).setTextAlignment(QtCore.Qt.AlignCenter)

                self.tableWidgetGP.item(rcount,0).setFlags(self.tableWidgetGP.item(rcount,0).flags() & ~QtCore.Qt.ItemIsEditable)
                self.tableWidgetGP.item(rcount,1).setFlags(self.tableWidgetGP.item(rcount,1).flags() & ~QtCore.Qt.ItemIsEditable)




                if j==i or j<i:
                    self.tableWidgetGP.setItem(rcount,5, QTableWidgetItem(str("-")))
                    self.tableWidgetKKS2.setItem(rcount,4, QTableWidgetItem(str("-")))

                else:
                    self.tableWidgetGP.setItem(rcount,5, QTableWidgetItem(str("")))
                    self.tableWidgetKKS2.setItem(rcount,4, QTableWidgetItem(str("")))

                if i != (noP_value-1) and j!= (noP_value-1) and i!=j:
                    #GP Ceq Cfil Cslope
                    self.tableWidgetGP.setItem(rcount,2, QTableWidgetItem(str("-")))
                    self.tableWidgetGP.setItem(rcount,3, QTableWidgetItem(str("-")))
                    self.tableWidgetGP.setItem(rcount,4, QTableWidgetItem(str("-")))

                    #CH Ceq Cfil
                    self.tableWidgetCH.setItem(rcount,2, QTableWidgetItem(str("-")))
                    self.tableWidgetCH.setItem(rcount,3, QTableWidgetItem(str("-")))

                    #KKS ceq
                    self.tableWidgetKKS.setItem(rcount,2, QTableWidgetItem(str("-")))

                    #KSS2 Ceq Cfill
                    self.tableWidgetKKS2.setItem(rcount,2, QTableWidgetItem(str("-")))
                    self.tableWidgetKKS2.setItem(rcount,3, QTableWidgetItem(str("-")))

                #KKS
                self.tableWidgetKKS.setItem(rcount,0, QTableWidgetItem(str(i)))
                self.tableWidgetKKS.setItem(rcount,1, QTableWidgetItem(str(j)))
                self.tableWidgetKKS.item(rcount,0).setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidgetKKS.item(rcount,1).setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidgetKKS.item(rcount,0).setFlags(self.tableWidgetKKS.item(rcount,0).flags() & ~QtCore.Qt.ItemIsEditable)
                self.tableWidgetKKS.item(rcount,1).setFlags(self.tableWidgetKKS.item(rcount,1).flags() & ~QtCore.Qt.ItemIsEditable)

                #KKS2
                self.tableWidgetKKS2.setItem(rcount,0, QTableWidgetItem(str(i)))
                self.tableWidgetKKS2.setItem(rcount,1, QTableWidgetItem(str(j)))
                self.tableWidgetKKS2.item(rcount,0).setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidgetKKS2.item(rcount,1).setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidgetKKS2.item(rcount,0).setFlags(self.tableWidgetKKS2.item(rcount,0).flags() & ~QtCore.Qt.ItemIsEditable)
                self.tableWidgetKKS2.item(rcount,1).setFlags(self.tableWidgetKKS2.item(rcount,1).flags() & ~QtCore.Qt.ItemIsEditable)


                #CH
                self.tableWidgetCH.setItem(rcount,0, QTableWidgetItem(str(i)))
                self.tableWidgetCH.setItem(rcount,1, QTableWidgetItem(str(j)))
                self.tableWidgetCH.item(rcount,0).setTextAlignment(QtCore.Qt.AlignCenter)
                self.tableWidgetCH.item(rcount,1).setTextAlignment(QtCore.Qt.AlignCenter)

                self.tableWidgetCH.item(rcount,0).setFlags(self.tableWidgetCH.item(rcount,0).flags() & ~QtCore.Qt.ItemIsEditable)
                self.tableWidgetCH.item(rcount,1).setFlags(self.tableWidgetCH.item(rcount,1).flags() & ~QtCore.Qt.ItemIsEditable)

                rcount = rcount +1


    def componentBtnClicked(self):
        self.pwidget_2.show()  #component Widget
        self.next2.setEnabled(False)
        self.componentbtn.setEnabled(False)
        self.phasebtn.setEnabled(False)



    def componentSaveBtnClicked(self):
        Cnames = self.ctext.toPlainText().splitlines()

        if len(Cnames) != self.noC.value():
            self.cerror.setText( str(self.noC.value()) + " Components required" )
        else:
            self.pwidget_2.hide()
            self.next2.setEnabled(True)
            self.componentbtn.setEnabled(True)
            self.phasebtn.setEnabled(True)
            self.cerror.setText( "" )


    def updateNoC(self):
        noC_value = self.noC.value()
        Cnames = self.ctext.toPlainText().splitlines()

        if len(Cnames) < noC_value :
            Com_text2 = self.ctext.toPlainText()

            for i in range(noC_value - len(Cnames) ):
                Com_text2 = Com_text2 +"\nC" +str(len(Cnames)+1+i)

            self.ctext.setPlainText(Com_text2)

        if len(Cnames) > noC_value:
            Com_text2 = Cnames[0]
            for i in range(1,noC_value,1):
                Com_text2 = Com_text2 + "\n" + Cnames[i]

            self.ctext.setPlainText(Com_text2)

        #Changing input length of Diffusion

        diffData = str(self.diffInput.text())
        matData = diffData.split(",")

        k=self.noC.value()-1

        if len(matData) > k and self.diffR_2.isChecked():
            ReducedText = matData[0]
            for i in range(1,k ,1):
                ReducedText = ReducedText + "," + matData[i]

            self.diffInput.setText(ReducedText)

        if len(matData) > k*k and self.diffR.isChecked():
            ReducedText = matData[0]
            for i in range(1,k*k ,1):
                ReducedText = ReducedText + "," + matData[i]

            self.diffInput.setText(ReducedText)


    def clickedBtn1(self):

        #frame Hide/Show
        self.frame_1.show()
        self.frame_2.hide()
        self.Second_widget.hide()
        self.Third_widget.hide()
        self.Four_widget.hide()
        self.Fifth_widget.hide()
        self.Sixth_widget.hide()
        self.Seven_widget.hide()
        self.First_widget.show()

        #Btn Animation
        self.btn1.setGeometry(60, 20, 300, 70)
        self.btn2.setGeometry(360, 30, 300, 60)


        self.btn1.setStyleSheet("background-color: rgb(64, 140, 191); border:none ;color:#fff ")
        self.btn2.setStyleSheet("background-color: rgb(238, 238, 236)")

        self.Qbox.show()
        self.Qbox.setStyleSheet("background-color: rgb(218, 218, 218); border: 1px solid rgb(77, 77, 77);")

    def clickedBtn2(self):

        if(self.dim.value() <= 1 or self.dim.value() > 3 ):
            self.error1.setText("Dimension should be 2D or 3D")
            return

        elif (self.mesh_x.text() == "" or int(self.mesh_x.text()) < 1):
            self.error1.setText("Please Fill valid MESH - X")
            return

        elif (self.mesh_y.text() == "" or int(self.mesh_x.text()) < 1):
            self.error1.setText("Please Fill valid MESH - Y")
            return

        elif (self.mesh_z.text() == "" or int(self.mesh_x.text()) < 1):
            self.error1.setText("Please Fill valid MESH - Z")
            return

        else:
            self.error1.setText("")

        self.frame_2.show()
        self.frame_1.hide()
        self.Second_widget.hide()
        self.Third_widget.hide()
        self.Four_widget.hide()
        self.Fifth_widget.hide()
        self.Sixth_widget.hide()
        self.Seven_widget.hide()
        self.First_widget.show()

        self.btn1.setGeometry(60, 30, 300, 60)
        self.btn2.setGeometry(360, 20, 300, 70)

        self.btn2.setStyleSheet("background-color: rgb(64, 140, 191); border:none ;color:#fff ")
        self.btn1.setStyleSheet("background-color: rgb(238, 238, 236)")

        self.Qbox.show()


    def clickedBtn3(self):

        #frame Hide/Show
        self.frame_6.hide()
        self.First_widget.hide()
        self.Second_widget.hide()
        self.Third_widget.hide()
        self.Fifth_widget.hide()
        self.Sixth_widget.hide()
        self.Seven_widget.hide()

        self.Qbox.hide()

        self.Four_widget.show()
        self.frame_5.show()

        #Btn Animation
        self.btn3.setGeometry(60, 20, 300, 70)
        self.btn4.setGeometry(360, 30, 300, 60)


        self.btn3.setStyleSheet("background-color: rgb(64, 140, 191); border:none ;color:#fff ")
        self.btn4.setStyleSheet("background-color: rgb(238, 238, 236)")


    def clickedBtn4(self):

        if self.phaseSave():

            k = self.noP.value()
            l = self.noC.value() -1

            for i in range(k):
                if self.DiffusivityType[i] == "0" and len(self.Diffusivity[i].split(",")) != l*l:
                    return

                if self.DiffusivityType[i] == "1" and ( len(self.Diffusivity[i].split(",")) < l or len(self.Diffusivity[i].split(",")) > l*l )  :
                    return

                if len(self.eigenStrain[i].split(",")) != 6:
                    return

                if self.elasticType == "0" and len(self.elasticConstant[i].split(",")) != 3:
                    return

                if self.elasticType == "1" and len(self.elasticConstant[i].split(",")) != 3:
                    return

                if self.elasticType == "2" and len(self.elasticConstant[i].split(",")) != 6:
                    return
        else:
            return

        self.error6.setText("")

        #frame Hide/Show
        self.frame_5.hide()
        self.First_widget.hide()
        self.Second_widget.hide()
        self.Third_widget.hide()
        self.Fifth_widget.hide()
        self.Sixth_widget.hide()
        self.Seven_widget.hide()

        self.Qbox.hide()

        self.Four_widget.show()
        self.frame_6.show()


        #Btn Animation
        self.btn3.setGeometry(60, 30, 300, 60)
        self.btn4.setGeometry(360, 20, 300, 70)


        self.btn4.setStyleSheet("background-color: rgb(64, 140, 191); border:none ;color:#fff ")
        self.btn3.setStyleSheet("background-color: rgb(238, 238, 236)")


    def clickedBtn5(self):

        #frame Hide/Show
        self.frame_8.show()
        self.frame_9.hide()
        self.frame_11.hide()
        self.First_widget.hide()
        self.Second_widget.hide()
        self.Third_widget.hide()
        self.Four_widget.hide()
        self.Fifth_widget.hide()
        self.Sixth_widget.hide()
        self.Seven_widget.show()

        self.Qbox.hide()

        #Btn Animation
        self.btn5.setGeometry(60, 20, 200, 70)
        self.btn6.setGeometry(260, 30, 200, 60)
        self.btn7.setGeometry(460, 30, 200, 60)


        self.btn5.setStyleSheet("background-color: rgb(64, 140, 191); border:none ;color:#fff ")
        self.btn6.setStyleSheet("background-color: rgb(238, 238, 236)")
        self.btn7.setStyleSheet("background-color: rgb(238, 238, 236)")


    def clickedBtn6(self):


        if self.radio_GP.isChecked() == False and self.radio_CH.isChecked() == False and self.radio_KKR.isChecked() == False and self.radio_KKS2.isChecked() == False:
            self.error8.setText("Please select a model")
            return

        self.error8.setText("")

        #frame Hide/Show
        self.frame_8.hide()
        self.frame_11.hide()
        self.First_widget.hide()
        self.Second_widget.hide()
        self.Third_widget.hide()
        self.Four_widget.hide()
        self.Fifth_widget.hide()
        self.Sixth_widget.hide()
        self.Seven_widget.show()


        self.Qbox.hide()
        self.frame_9.show()


        #Btn Animation
        self.btn5.setGeometry(60, 30, 200, 60)
        self.btn6.setGeometry(260, 20, 200, 70)
        self.btn7.setGeometry(460, 30, 200, 60)


        self.btn6.setStyleSheet("background-color: rgb(64, 140, 191); border:none ;color:#fff ")
        self.btn5.setStyleSheet("background-color: rgb(238, 238, 236)")
        self.btn7.setStyleSheet("background-color: rgb(238, 238, 236)")


    def clickedBtn7(self):

        if self.radio_GP.isChecked() and self.saveGPChack() or self.radio_KKR.isChecked() and self.saveKKSCheck() or self.radio_KKS2.isChecked() and self.saveKKS2Check() or self.radio_CH.isChecked() and self.saveGPChack():

            self.frame_8.hide()
            self.frame_9.hide()
            self.First_widget.hide()
            self.Second_widget.hide()
            self.Third_widget.hide()
            self.Four_widget.hide()
            self.Fifth_widget.hide()
            self.Sixth_widget.hide()
            self.Seven_widget.show()


            self.Qbox.hide()
            self.frame_11.show()


            #Btn Animation
            self.btn5.setGeometry(60, 30, 200, 60)
            self.btn6.setGeometry(260, 30, 200, 60)
            self.btn7.setGeometry(460, 20, 200, 70)


            self.btn7.setStyleSheet("background-color: rgb(64, 140, 191); border:none ;color:#fff ")
            self.btn5.setStyleSheet("background-color: rgb(238, 238, 236)")
            self.btn6.setStyleSheet("background-color: rgb(238, 238, 236)")



    def NextBtn1(self):

        if (self.dx.text() == ""):
            self.error2.setText("Please Fill valid dx")
            return

        elif (self.dy.text() == ""):
            self.error2.setText("Please Fill valid Dy")
            return

        elif (self.dz.text() == ""):
            self.error2.setText("Please Fill valid dz")
            return

        elif (self.dt.text() == ""):
            self.error2.setText("Please Fill valid Dt")
            return

        else:
            self.error2.setText("")

        self.First_widget.hide()
        self.Four_widget.hide()
        self.Fifth_widget.hide()
        self.Sixth_widget.hide()
        self.Seven_widget.hide()
        self.Third_widget.hide()
        self.Qbox.hide()
        self.Second_widget.show()

        self.sideBtn2.setGeometry(0,180,220,60)
        self.sideBtn2.setStyleSheet('background-color: rgb(171, 196, 223);font: 10pt "Ubuntu";')
        self.sideBtn2.setEnabled(True)


    def NextBtn2(self):
        self.First_widget.hide()
        self.Second_widget.hide()
        self.Four_widget.hide()
        self.Fifth_widget.hide()
        self.Sixth_widget.hide()
        self.Seven_widget.hide()
        self.Third_widget.show()

        self.sideBtn3.setGeometry(0,240,220,60)
        self.sideBtn3.setStyleSheet('background-color: rgb(171, 196, 223);font: 10pt "Ubuntu";')
        self.sideBtn3.setEnabled(True)
        self.Qbox.hide()


    def NextBtn3(self):
        if (self.timeSteps.text() == ""):
            self.error4.setText("Please Fill valid TimeSteps")
            return

        elif (self.Nsmooth.text() == ""):
            self.error4.setText("Please Fill valid Nsmooth")
            return

        elif (self.saveAt.text() == ""):
            self.error4.setText("Please Fill valid Save Interval")
            return

        elif (self.startTime.text() == ""):
            self.error4.setText("Please Fill valid Start Time")
            return

        else:
            self.error4.setText("")
        
        self.First_widget.hide()
        self.Second_widget.hide()
        self.Third_widget.hide()
        self.Four_widget.show()
        self.Fifth_widget.hide()
        self.Sixth_widget.hide()
        self.Seven_widget.hide()

        self.sideBtn4.setGeometry(0,300,220,60)
        self.sideBtn4.setStyleSheet('background-color: rgb(171, 196, 223);font: 10pt "Ubuntu";')
        self.sideBtn4.setEnabled(True)
        self.Qbox.hide()

        k = self.noC.value()-1

        if k<5:
                self.diffMat.setGeometry(160-(28*k), 150-(23*k), 56*k, 46*k)
                self.line_2.setGeometry(0,46*k-2,10,2)
                self.line_3.setGeometry(56*k-10,0,10,2)
                self.line_4.setGeometry(56*k-10,46*k-2,10,2)
        else:
            self.diffMat.setGeometry(48, 58, 224, 184)
            self.line_2.setGeometry(0,182,10,2)
            self.line_3.setGeometry(214,0,10,2)
            self.line_4.setGeometry(214,182,10,2)


        Wlen = (len(self.diffMat.children()) - 5)**0.5

        if Wlen == 0:
            self.diffMatIn = [[0 for x in range(20)] for y in range(20)]

            for i in range(k):
                for j in range(k):
                    self.diffMatIn[i][j] = QLabel()
                    self.diffMatIn[i][j].setText("D"+str(i+1)+str(j+1))
                    self.diffMatIn[i][j].setAlignment(QtCore.Qt.AlignCenter)
                    self.diffMatIn[i][j].setStyleSheet("color : #fff ; font: 75 11pt 'Ubuntu';")
                    if k<5:
                        self.diffMatIn[i][j].setFixedHeight(40)
                        self.diffMatIn[i][j].setStyleSheet("color : #fff ; font: 75 10pt 'Ubuntu';")

                    self.diffMat.layout().addWidget(self.diffMatIn[i][j], i,j)

        elif k < Wlen:
            for i in range(int(Wlen)):
                for j in range(int(Wlen)):
                    if i > k-1 or j > k-1 :
                        self.diffMatIn[i][j].deleteLater()

        elif k > Wlen:
            for i in range(k):
                for j in range(k):
                    if i > int(Wlen-1) or j > int(Wlen-1) :

                        self.diffMatIn[i][j] = QLabel()

                        #filling diffusion matrix based on condition
                        if self.diffR_2.isChecked():
                            if i ==j :
                                self.diffMatIn[i][j].setText("D"+str(i+1)+str(j+1))
                            else:
                                self.diffMatIn[i][j].setText("-")
                        elif self.diffR.isChecked():
                            self.diffMatIn[i][j].setText("D"+str(i+1)+str(j+1))


                        self.diffMatIn[i][j].setAlignment(QtCore.Qt.AlignCenter)
                        self.diffMatIn[i][j].setStyleSheet("color : #fff ; font: 75 11pt 'Ubuntu';")
                        if k<5:
                            self.diffMatIn[i][j].setFixedHeight(40)
                            self.diffMatIn[i][j].setStyleSheet("color : #fff ; font: 75 10pt 'Ubuntu';")

                        self.diffMat.layout().addWidget(self.diffMatIn[i][j], i,j)

        if self.elasticType[0] != '':

            if self.elasticType[0] == '0':
                self.es.setChecked(True)
                self.es_2.setChecked(False)
                self.es_3.setChecked(False)

            elif self.elasticType[0] == '1':
                self.es.setChecked(False)
                self.es_2.setChecked(True)
                self.es_3.setChecked(False)

            elif self.elasticType[0] == '2':
                self.es.setChecked(False)
                self.es_2.setChecked(False)
                self.es_3.setChecked(True)

        if self.DiffusivityType[0] !='':

            if self.DiffusivityType[0] == '0':
                self.diffR_2.setChecked(True)
                self.diffR_2.setChecked(False)
                self.diffR.setChecked(True)

            elif self.DiffusivityType[0] == '1':
                self.diffR.setChecked(True)
                self.diffR.setChecked(False)
                self.diffR_2.setChecked(True)


    def NextBtn4(self):

        gammaData = self.gammaInput.text().split(",")

        k=self.noP.value()
        max_len = k*((k -1 )/2)


        if self.gammaInput.text() == "":
            self.error6.setText("Please fill Gamma Value")
            return

        elif len(gammaData) != max_len:
            self.error6.setText("Invalid Gamma tuple length")
            return

        elif self.R_Value.text()=="":
            self.error6.setText("Please fill R Value")
            return

        elif self.V_Value.text()=="":
            self.error6.setText("Please fill V Value")
            return

        else:
            self.error6.setText("")

        self.First_widget.hide()
        self.Second_widget.hide()
        self.Four_widget.hide()
        self.Third_widget.hide()
        self.Sixth_widget.hide()
        self.Seven_widget.hide()
        self.Fifth_widget.show()

        self.sideBtn5.setGeometry(0,360,220,60)
        self.sideBtn5.setStyleSheet('background-color: rgb(171, 196, 223);font: 10pt "Ubuntu";')
        self.sideBtn5.setEnabled(True)
        self.Qbox.show()

    def NextBtn5(self):

        if self.phaseSave_BC():


            if self.BconV[0] =="" and len(self.BconV[0].split(",")) != 4:
                self.error7.setText("Please fill Boundary condtions Phi")
                return

            elif self.BconV[1] =="" and len(self.BconV[1].split(",")) != 4 and self.BconV[2] =="" and len(self.BconV[2].split(",")) != 4:
                self.error7.setText("Please fill Boundary condtions mu/c")
                return

            elif self.BconV[3] =="" and len(self.BconV[3].split(",")) != 4:
                self.error7.setText("Please fill Boundary condtions T")
                return
            else:
                self.error7.setText("")

        else:
            return


        self.addShape.setText("Add " + self.shape.currentText() +  " | "+self.pDropdown_3.currentText())

        self.First_widget.hide()
        self.Second_widget.hide()
        self.Four_widget.hide()
        self.Third_widget.hide()
        self.Fifth_widget.hide()
        self.Seven_widget.hide()
        self.Sixth_widget.show()

        self.sideBtn6.setGeometry(0,420,220,60)
        self.sideBtn6.setStyleSheet('background-color: rgb(171, 196, 223);font: 10pt "Ubuntu";')
        self.sideBtn6.setEnabled(True)
        self.Qbox.hide()

    def NextBtn6(self):

        if self.phaseSave():
            self.error6.setText("")
        else:
            return

        if self.phaseSave_BC():
            self.error6.setText("")
        else:
            return

        if self.ShapeList.count() == 0 and self.ShapeFlag == 0:
            self.error10.setText("required atleast 1 filling condition")
            return
        self.error10.setText("")
        self.First_widget.hide()
        self.Second_widget.hide()
        self.Four_widget.hide()
        self.Third_widget.hide()
        self.Fifth_widget.hide()
        self.Sixth_widget.hide()
        self.Seven_widget.show()

        self.sideBtn7.setGeometry(0,480,220,60)
        self.sideBtn7.setStyleSheet('background-color: rgb(171, 196, 223);font: 10pt "Ubuntu";')
        self.sideBtn7.setEnabled(True)
        self.Qbox.hide()


    def FillDiffMat(self):
        diffData = str(self.diffInput.text())
        matData = diffData.split(",")
        k=self.noC.value()-1

        if len(matData) > k*k and self.diffR.isChecked():
            ReducedText = matData[0]
            for i in range(1,k*k ,1):
                ReducedText = ReducedText + "," + matData[i]

            self.diffInput.setText(ReducedText)
            return

        if len(matData) > k and self.diffR_2.isChecked():
            ReducedText = matData[0]
            for i in range(1,k ,1):
                ReducedText = ReducedText + "," + matData[i]

            self.diffInput.setText(ReducedText)
            return


        diffarray = [None]*k

        for i in range(k):
            diffarray[i] = self.diffMatIn[i][i]

        if self.diffR.isChecked():
            for i in range(k):
                for j in range(k):
                    if i!=j:
                        diffarray.append(self.diffMatIn[i][j])

        for i in range(len(matData)):
            diffarray[i].setText(matData[i])

        for i in range(k):
            for j in range(k):
                if self.diffMatIn[i][j].text() == "":
                    self.diffMatIn[i][j].setText("D"+str(i+1)+str(j+1))


    def  dMatrixToggled(self):
        diffData = str(self.diffInput.text())
        matData = diffData.split(",")

        k=self.noC.value()-1

        if len(matData) > k and self.diffR_2.isChecked():
            ReducedText = matData[0]
            for i in range(1,k ,1):
                ReducedText = ReducedText + "," + matData[i]

            self.diffInput.setText(ReducedText)

        for i in range(k):
            for j in range(k):
                if i!=j:
                    self.diffMatIn[i][j].setText("-")


    def  fMatrixToggled(self):
        diffData = str(self.diffInput.text())
        matData = diffData.split(",")

        k=self.noC.value()-1

        for i in range(k):
            for j in range(k):
                if i!=j:
                    if self.diffMatIn[i][j].text() == "-":
                        self.diffMatIn[i][j].setText("D"+str(i+1)+str(j+1))



    def FillGammaMat(self):

        self.error6.setText("")
        gammaData = self.gammaInput.text()
        matData = gammaData.split(",")
        k=self.noP.value()
        max_len = k*((k -1 )/2)

        if len(matData) > max_len:
            ReducedText = matData[0]
            for i in range(1,int(max_len) ,1):
                ReducedText = ReducedText + "," + matData[i]

            self.gammaInput.setText(ReducedText)
            return

    def phaseChange(self):
        currentPhase = self.pDropdown.currentIndex()

        if currentPhase == 0:
            self.allCheck.hide()

        else:
            self.allCheck.show()


        if currentPhase > int(self.marker.text()) and self.phaseSave():

            self.marker.setText(str(currentPhase ) )
            if self.Diffusivity[currentPhase] == "":
                self.phaseReset()
            else:
                self.phaseRetrive()

            self.error5.setText("")

        elif currentPhase < int(self.marker.text()) and self.phaseSave() :
            self.phaseRetrive()
            self.marker.setText(str(currentPhase ))
            return

        else:
            self.pDropdown.setCurrentIndex(int(self.marker.text()))
            return



    def phaseReset(self):
        self.allCheck.setChecked(False)
        self.diffR.setChecked(True)
        self.es.setChecked(True)

        self.diffInput.setText("")
        self.Estrain.setText("0.01,0.01,0.0,0.0,0.0,0.0")
        self.Econstant.setText("")

        k=self.noC.value()-1

        for i in range(k):
            for j in range(k):
                self.diffMatIn[i][j].setText("D"+str(i+1)+str(j+1))

    def phaseRetrive(self):
        self.marker.setText(str(self.pDropdown.currentIndex()) )
        marker = int(self.marker.text())
        k=self.noC.value()-1
        diffInputData = self.Diffusivity[marker].split(",")

        if self.DiffusivityType[marker] == "0":
            self.diffR.setChecked(True)
            self.diffR_2.setChecked(False)

            p=0
            for i in range(k):
                for j in range(k):
                    if p < len(diffInputData):
                        self.diffMatIn[i][j].setText(diffInputData[p])
                        p = p+1
                    else:
                        self.diffMatIn[i][j].setText("D"+str(i+1)+str(j+1))


        elif self.DiffusivityType[marker] == "1":
            self.diffR_2.setChecked(True)
            self.diffR.setChecked(False)

            q=0
            for i in range(k):
                for j in range(k):
                    if i==j and q < len(diffInputData):
                        self.diffMatIn[i][j].setText(diffInputData[q])
                        q = q+1
                    else:
                        self.diffMatIn[i][j].setText("-")

        self.diffInput.setText(self.Diffusivity[marker])
        self.Estrain.setText(self.eigenStrain[marker])

        if self.elasticType[marker] == "0" :
            self.es.setChecked(True)
            self.es_2.setChecked(False)
            self.es_3.setChecked(False)

        elif self.elasticType[marker] == "1" :
            self.es_2.setChecked(True)
            self.es.setChecked(False)
            self.es_3.setChecked(False)

        elif self.elasticType[marker] == "2" :
            self.es_3.setChecked(True)
            self.es_2.setChecked(False)
            self.es.setChecked(False)

        self.Econstant.setText(self.elasticConstant[marker])
        self.allCheck.setChecked(False)



    def phaseSave(self):

        k=self.noC.value()-1
        marker = int(self.marker.text())
        diffInputData = self.diffInput.text().split(",")
        EstrainData = self.Estrain.text().split(",")
        EconstantData = self.Econstant.text().split(",")

        if self.diffInput.text() =="":
            self.error5.setText("Please fill Diffusivity")
            return False

        elif len(diffInputData) != k*k and self.diffR.isChecked():
            self.error5.setText("Invalid Diffusivity tuple length")
            return False

        elif len(diffInputData) != k and self.diffR_2.isChecked():
            self.error5.setText("Invalid Diffusivity tuple length")
            return False

        elif self.Estrain.text() =="":
            self.error5.setText("Please fill Eigen Strain")
            return False

        elif len(EstrainData) != 6:
            self.error5.setText("Invalid Eigen Strain tuple length")
            return False

        elif self.Econstant.text() =="":
            self.error5.setText("Please fill Elastic Constant")
            return False

        elif len(EconstantData) != 3 and self.es.isChecked():
            self.error5.setText("Invalid Elastic Constant tuple length")
            return False

        elif len(EconstantData) != 3 and self.es_2.isChecked():
            self.error5.setText("Invalid Elastic Constant tuple length")
            return False

        elif len(EconstantData) != 6 and self.es_3.isChecked():
            self.error5.setText("Invalid Elastic Constant tuple length")
            return False

        else:
            if self.diffR.isChecked():
                self.DiffusivityType[marker] = "0"

            elif self.diffR_2.isChecked():
                self.DiffusivityType[marker] = "1"

            self.Diffusivity[marker] = self.diffInput.text()

            self.eigenStrain[marker] = self.Estrain.text()

            if self.es.isChecked():
                self.elasticType[marker] = "0"

            elif self.es_2.isChecked():
                self.elasticType[marker] = "1"

            elif self.es_3.isChecked():
                self.elasticType[marker] = "2"

            self.elasticConstant[marker] = self.Econstant.text()

            return True

    def allCheckFunc(self):

        if self.allCheck.isChecked():

            marker = self.pDropdown.currentIndex()-1
            k=self.noC.value()-1
            diffInputData = self.Diffusivity[marker].split(",")

            if self.DiffusivityType[marker] == "0":
                self.diffR.setChecked(True)
                self.diffR_2.setChecked(False)

                p=0
                for i in range(k):
                    for j in range(k):
                        self.diffMatIn[i][j].setText(diffInputData[p])
                        p = p+1

            elif self.DiffusivityType[marker] == "1":
                self.diffR_2.setChecked(True)
                self.diffR.setChecked(False)

                q=0
                for i in range(k):
                    for j in range(k):
                        if i==j:
                            self.diffMatIn[i][j].setText(diffInputData[q])
                            q = q+1

            self.diffInput.setText(self.Diffusivity[marker])
            self.Estrain.setText(self.eigenStrain[marker])

            if self.elasticType[marker] == "0" :
                self.es.setChecked(True)
                self.es_2.setChecked(False)
                self.es_3.setChecked(False)

            elif self.elasticType[marker] == "1" :
                self.es_2.setChecked(True)
                self.es.setChecked(False)
                self.es_3.setChecked(False)

            elif self.elasticType[marker] == "2" :
                self.es_3.setChecked(True)
                self.es_2.setChecked(False)
                self.es.setChecked(False)

            self.Econstant.setText(self.elasticConstant[marker])
        else:
            return
            #self.phaseReset()

    def esToggled(self):
        self.es.setChecked(True)
        return

    def es2Toggled(self):
        self.es_2.setChecked(True)
        return

    def es3Toggled(self):
        self.es_3.setChecked(True)
        return


    #Boundary Frame Functions

    def phaseChange_BC(self):

        if self.phaseSave_BC():

            current_Index = self.pDropdown_2.currentIndex()

            if current_Index == 0:
                self.allCheck_2.hide()
            else:
                self.allCheck_2.show()


            if self.Bcnd[current_Index] == "" and self.BconV[current_Index] =="":
                self.phaseReset_BC()
            else:
                self.phaseRetrive_BC()

            if self.pDropdown_2.currentIndex() ==0:
                self.marker_bc.setText("0")

            elif self.pDropdown_2.currentIndex() == 1:
                self.marker_bc.setText("1")

            elif self.pDropdown_2.currentIndex() == 2:
                self.marker_bc.setText("2")

            elif self.pDropdown_2.currentIndex() == 3:
                self.marker_bc.setText("3")


        else:
            self.pDropdown_2.setCurrentIndex(int(self.marker_bc.text()))

    def phaseReset_BC(self):

        self.BC_1.setCurrentIndex(0)
        self.BC_2.setCurrentIndex(0)
        self.BC_3.setCurrentIndex(0)
        self.BC_4.setCurrentIndex(0)

        self.allCheck_BC.setChecked(False)
        self.allCheck_2.setChecked(False)


        self.BCV_1.setText("0")
        self.BCV_2.setText("0")
        self.BCV_3.setText("0")
        self.BCV_4.setText("0")

    def phaseSave_BC(self):

        if self.BCV_1.text()=="":
            self.error7.setText("Please fill Boundary Value for X+")
            return False

        elif self.BCV_2.text()=="":
            self.error7.setText("Please fill Boundary Value for X-")
            return False

        elif self.BCV_3.text()=="":
            self.error7.setText("Please fill Boundary Value for Y+")
            return False

        elif self.BCV_4.text()=="":
            self.error7.setText("Please fill Boundary Value for Y-")
            return False

        else:

            self.Bcnd[int(self.marker_bc.text())] =str(self.BC_1.currentIndex()) + "," + str(self.BC_2.currentIndex()) + "," + str(self.BC_3.currentIndex()) + "," + str(self.BC_4.currentIndex())
            self.BconV[int(self.marker_bc.text())] = self.BCV_1.text() + "," + self.BCV_2.text() + "," + self.BCV_3.text() + "," + self.BCV_4.text()
            self.error7.setText("")
            self.Qbox.setStyleSheet("background-color: rgb(218, 218, 218); border: 1px solid rgb(77, 77, 77);")
            return True


    def phaseRetrive_BC(self):
        current_Index = self.pDropdown_2.currentIndex()

        Bcondarray = self.Bcnd[current_Index].split(",")
        self.BC_1.setCurrentIndex(int(Bcondarray[0]))
        self.BC_2.setCurrentIndex(int(Bcondarray[1]))
        self.BC_3.setCurrentIndex(int(Bcondarray[2]))
        self.BC_4.setCurrentIndex(int(Bcondarray[3]))

        BcondVarray = self.BconV[current_Index].split(",")
        self.BCV_1.setText(BcondVarray[0])
        self.BCV_2.setText(BcondVarray[1])
        self.BCV_3.setText(BcondVarray[2])
        self.BCV_4.setText(BcondVarray[3])


    def allCheckBC(self):
        current_Index = self.pDropdown_2.currentIndex()

        if self.allCheck_2.isChecked() and self.Bcnd[current_Index-1] != "" and self.BconV[current_Index-1] != "":

            Bcondarray = self.Bcnd[current_Index-1].split(",")
            self.BC_1.setCurrentIndex(int(Bcondarray[0]))
            self.BC_2.setCurrentIndex(int(Bcondarray[1]))
            self.BC_3.setCurrentIndex(int(Bcondarray[2]))
            self.BC_4.setCurrentIndex(int(Bcondarray[3]))

            BcondVarray = self.BconV[current_Index-1].split(",")
            self.BCV_1.setText(BcondVarray[0])
            self.BCV_2.setText(BcondVarray[1])
            self.BCV_3.setText(BcondVarray[2])
            self.BCV_4.setText(BcondVarray[3])


    def allCheckBCV(self):

        if self.allCheck_BC.isChecked():

            self.BC_2.setCurrentIndex(self.BC_1.currentIndex())
            self.BC_3.setCurrentIndex(self.BC_1.currentIndex())
            self.BC_4.setCurrentIndex(self.BC_1.currentIndex())
            self.BCV_2.setText(self.BCV_1.text())
            self.BCV_3.setText(self.BCV_1.text())
            self.BCV_4.setText(self.BCV_1.text())

        else:
            self.BC_2.setCurrentIndex(0)
            self.BC_3.setCurrentIndex(0)
            self.BC_4.setCurrentIndex(0)
            self.BCV_2.setText("")
            self.BCV_3.setText("")
            self.BCV_4.setText("")


    def BCV1fill(self):
        BC_h = self.Qbox.frameGeometry().height()
        BC_w = self.Qbox.frameGeometry().width()
        BC_l = self.Qbox.frameGeometry().left()
        BC_t = self.Qbox.frameGeometry().top()

        self.Qbox.setStyleSheet("background-color: rgb(218, 218, 218); border-right: 4px solid red;")

    def BCV2fill(self):
        self.Qbox.setStyleSheet("background-color: rgb(218, 218, 218); border-left: 4px solid red;")

    def BCV3fill(self):
        self.Qbox.setStyleSheet("background-color: rgb(218, 218, 218); border-top: 4px solid red;")


    def BCV4fill(self):
        self.Qbox.setStyleSheet("background-color: rgb(218, 218, 218); border-bottom: 4px solid red;")


    def BCV1Change(self):

        if self.BC_1.currentIndex() == 1:
            self.BCV_1.setText("0")
            self.BCV_1.setEnabled(False)

        elif  self.BC_1.currentIndex() == 3:
            self.BC_2.setCurrentIndex(3)
            self.BCV_1.setText("0")
            self.BCV_2.setText("0")
            self.BCV_1.setEnabled(False)
            self.BCV_2.setEnabled(False)

        else:
            self.BCV_1.setEnabled(True)


        if self.BC_1.currentIndex() !=3 and self.BC_2.currentIndex() == 3:
            self.BC_2.setCurrentIndex(0)
            self.BCV_2.setEnabled(True)

    def BCV2Change(self):

        if self.BC_2.currentIndex() == 1:
            self.BCV_2.setText("0")
            self.BCV_2.setEnabled(False)

        elif  self.BC_2.currentIndex() == 3:
            self.BC_1.setCurrentIndex(3)
            self.BCV_1.setText("0")
            self.BCV_2.setText("0")
            self.BCV_1.setEnabled(False)
            self.BCV_2.setEnabled(False)

        else:
            self.BCV_2.setEnabled(True)


        if self.BC_2.currentIndex() !=3 and self.BC_1.currentIndex() == 3:
            self.BC_1.setCurrentIndex(0)
            self.BCV_1.setEnabled(True)

    def BCV3Change(self):

        if self.BC_3.currentIndex() == 1:
            self.BCV_3.setText("0")
            self.BCV_3.setEnabled(False)

        elif  self.BC_3.currentIndex() == 3:
            self.BC_4.setCurrentIndex(3)
            self.BCV_3.setText("0")
            self.BCV_4.setText("0")
            self.BCV_3.setEnabled(False)
            self.BCV_4.setEnabled(False)

        else:
            self.BCV_3.setEnabled(True)


        if self.BC_3.currentIndex() !=3 and self.BC_4.currentIndex() == 3:
            self.BC_4.setCurrentIndex(0)
            self.BCV_4.setEnabled(True)


    def BCV4Change(self):
        if self.BC_4.currentIndex() == 1:
            self.BCV_4.setText("0")
            self.BCV_4.setEnabled(False)

        elif  self.BC_4.currentIndex() == 3:
            self.BC_3.setCurrentIndex(3)
            self.BCV_3.setText("0")
            self.BCV_4.setText("0")
            self.BCV_3.setEnabled(False)
            self.BCV_4.setEnabled(False)

        else:
            self.BCV_4.setEnabled(True)


        if self.BC_4.currentIndex() !=3 and self.BC_3.currentIndex() == 3:
            self.BC_3.setCurrentIndex(0)
            self.BCV_3.setEnabled(True)


    def domainShapeChange(self):
        self.addShape.setText("Add " + self.shape.currentText() +  " | "+self.pDropdown_3.currentText())
        self.shapeFrameTitle.setText( self.shape.currentText() +  " | "+self.pDropdown_3.currentText())
        return

    def domainPhaseChange(self):
        self.addShape.setText("Add " + self.shape.currentText() +  " | "+self.pDropdown_3.currentText())
        self.shapeFrameTitle.setText( self.shape.currentText() +  " | "+self.pDropdown_3.currentText())
        return

    def shapeframeToggle(self):
        self.shapeframe.show()
        self.cube_end.setText("")
        self.cube_start.setText("")
        self.cylinder_center.setText("")
        self.cylinder_radius.setText("")
        self.cylinder_zend.setText("0")
        self.cylinder_zstart.setText("0")
        self.ellipse_center.setText("")
        self.ellipse_eccentric.setText("")
        self.ellipse_majorAxis.setText("")
        self.ellipse_rotation.setText("")
        self.sphere_center.setText("")
        self.sphere_radius.setText("")
        self.shapeSave.show()
        self.shapeUpdate.hide()
        self.shapeedit.setEnabled(False)
        self.shapedelete.setEnabled(False)

        if self.shape.currentIndex() ==0:
            self.fillCUBE.show()
            self.fillCYLINDER.hide()
            self.fillELLIPSE.hide()
            self.fillSPHERE.hide()
            return

        elif self.shape.currentIndex() ==1:
            self.fillCUBE.hide()
            self.fillCYLINDER.show()
            self.fillELLIPSE.hide()
            self.fillSPHERE.hide()
            return

        elif self.shape.currentIndex() ==2:
            self.fillCUBE.hide()
            self.fillCYLINDER.hide()
            self.fillELLIPSE.show()
            self.fillSPHERE.hide()
            return

        elif self.shape.currentIndex() ==3:
            self.fillCUBE.hide()
            self.fillCYLINDER.hide()
            self.fillELLIPSE.hide()
            self.fillSPHERE.show()
            return


    def shapeCancelClicked(self):
        self.shapeframe.hide()
        self.shapeedit.setEnabled(True)
        self.shapedelete.setEnabled(True)
        return

    def shapeSaveClicked(self):

        if self.shape.currentIndex() ==0:

            if self.cube_start.text() == "":
                self.shapeframe_error.setText("Please fill cube start point")
                return

            elif len(self.cube_start.text().split(",")) != 3:
                self.shapeframe_error.setText("Invalid cube start point")
                return

            elif self.cube_end.text() == "":
                self.shapeframe_error.setText("Please fill cube end point")
                return

            elif len(self.cube_end.text().split(",")) != 3:
                self.shapeframe_error.setText("Invalid cube end point")
                return

            else:
                self.ShapeList.addItem("CUBE {"+ str(self.pDropdown_3.currentIndex()) + "," + self.cube_start.text() + "," + self.cube_end.text()+"}" )
                self.shapeframe_error.setText("")


        elif self.shape.currentIndex() ==1:

            if self.cylinder_center.text() == "":
                self.shapeframe_error.setText("Please fill cylinder center point")
                return

            elif len(self.cylinder_center.text().split(",")) != 2:
                self.shapeframe_error.setText("Invalid cylinder center point")
                return

            elif self.cylinder_zstart.text() == "":
                self.shapeframe_error.setText("Please fill cylinder z-start point")
                return

            elif self.cylinder_zend.text() == "":
                self.shapeframe_error.setText("Please fill cylinder z-end point")
                return

            elif self.cylinder_radius.text() == "":
                self.shapeframe_error.setText("Please fill cylinder radius ")
                return

            else:
                self.ShapeList.addItem("CYLINDER {"+ str(self.pDropdown_3.currentIndex()) + "," + self.cylinder_center.text() + "," + self.cylinder_zstart.text() + "," +self.cylinder_zend.text() + "," + self.cylinder_radius.text() + "}")
                self.shapeframe_error.setText("")



        elif self.shape.currentIndex() ==2:
            if self.ellipse_center.text() == "":
                self.shapeframe_error.setText("Please fill ellipse center point")
                return

            elif len(self.ellipse_center.text().split(",")) != 2:
                self.shapeframe_error.setText("Invalid ellipse center point")
                return

            elif self.ellipse_majorAxis.text() == "":
                self.shapeframe_error.setText("Please fill ellipse major-axis point")
                return

            elif self.ellipse_eccentric.text() == "":
                self.shapeframe_error.setText("Please fill ellipse eccentricity point")
                return

            elif self.ellipse_rotation.text() == "":
                self.shapeframe_error.setText("Please fill ellipse rotation degree")
                return

            else:
                self.ShapeList.addItem("ELLIPSE {"+ str(self.pDropdown_3.currentIndex()) + "," + self.ellipse_center.text() + "," + self.ellipse_majorAxis.text() + "," +self.ellipse_eccentric.text() + "," + self.ellipse_rotation.text() + "}")
                self.shapeframe_error.setText("")


        elif self.shape.currentIndex() ==3:

            if self.sphere_center.text() == "":
                self.shapeframe_error.setText("Please fill sphere center point")
                return

            elif len(self.sphere_center.text().split(",")) != 3:
                self.shapeframe_error.setText("Invalid sphere center point")
                return

            elif self.sphere_radius.text() == "":
                self.shapeframe_error.setText("Please fill sphere radius")
                return

            else:
                self.ShapeList.addItem("SPHERE {"+ str(self.pDropdown_3.currentIndex()) + "," + self.sphere_center.text() + "," + self.sphere_radius.text()+"}" )
                self.shapeframe_error.setText("")

        self.shapeframe.hide()
        self.shapeedit.setEnabled(True)
        self.shapedelete.setEnabled(True)

    def shapeUpdateClicked(self):

        shapeText  = self.ShapeList.item(self.ShapeList.currentRow()).text()
        shapeText = shapeText.replace("{", "")
        shapeText = shapeText.replace("}", "")
        shapeData = shapeText.split(" ")

        if shapeData[0] == "CUBE":

            if self.cube_start.text() == "":
                self.shapeframe_error.setText("Please fill cube start point")
                return

            elif len(self.cube_start.text().split(",")) != 3:
                self.shapeframe_error.setText("Invalid cube start point")
                return

            elif self.cube_end.text() == "":
                self.shapeframe_error.setText("Please fill cube end point")
                return

            elif len(self.cube_end.text().split(",")) != 3:
                self.shapeframe_error.setText("Invalid cube end point")
                return

            else:
                self.ShapeList.item(self.ShapeList.currentRow()).setText("CUBE {"+ str(self.pDropdown_3.currentIndex()) + "," + self.cube_start.text() + "," + self.cube_end.text()+"}" )
                self.shapeframe_error.setText("")


        elif shapeData[0] == "CYLINDER":

            if self.cylinder_center.text() == "":
                self.shapeframe_error.setText("Please fill cylinder center point")
                return

            elif len(self.cylinder_center.text().split(",")) != 2:
                self.shapeframe_error.setText("Invalid cylinder center point")
                return

            elif self.cylinder_zstart.text() == "":
                self.shapeframe_error.setText("Please fill cylinder z-start point")
                return

            elif self.cylinder_zend.text() == "":
                self.shapeframe_error.setText("Please fill cylinder z-end point")
                return

            elif self.cylinder_radius.text() == "":
                self.shapeframe_error.setText("Please fill cylinder radius ")
                return

            else:
                self.ShapeList.item(self.ShapeList.currentRow()).setText("CYLINDER {"+ str(self.pDropdown_3.currentIndex()) + "," + self.cylinder_center.text() + "," + self.cylinder_zstart.text() + "," +self.cylinder_zend.text() + "," + self.cylinder_radius.text() + "}")
                self.shapeframe_error.setText("")


        elif shapeData[0] == "ELLIPSE":
            if self.ellipse_center.text() == "":
                self.shapeframe_error.setText("Please fill ellipse center point")
                return

            elif len(self.ellipse_center.text().split(",")) != 2:
                self.shapeframe_error.setText("Invalid ellipse center point")
                return

            elif self.ellipse_majorAxis.text() == "":
                self.shapeframe_error.setText("Please fill ellipse major-axis point")
                return

            elif self.ellipse_eccentric.text() == "":
                self.shapeframe_error.setText("Please fill ellipse eccentricity point")
                return

            elif self.ellipse_rotation.text() == "":
                self.shapeframe_error.setText("Please fill ellipse rotation degree")
                return

            else:
                self.ShapeList.item(self.ShapeList.currentRow()).setText("ELLIPSE {"+ str(self.pDropdown_3.currentIndex()) + "," + self.ellipse_center.text() + "," + self.ellipse_majorAxis.text() + "," +self.ellipse_eccentric.text() + "," + self.ellipse_rotation.text() + "}")
                self.shapeframe_error.setText("")


        elif shapeData[0] == "SPHERE":

            if self.sphere_center.text() == "":
                self.shapeframe_error.setText("Please fill sphere center point")
                return

            elif len(self.sphere_center.text().split(",")) != 3:
                self.shapeframe_error.setText("Invalid sphere center point")
                return

            elif self.sphere_radius.text() == "":
                self.shapeframe_error.setText("Please fill sphere radius")
                return

            else:
                self.ShapeList.item(self.ShapeList.currentRow()).setText("SPHERE {"+ str(self.pDropdown_3.currentIndex()) + "," + self.sphere_center.text() + "," + self.sphere_radius.text()+"}" )
                self.shapeframe_error.setText("")

        self.shapeframe.hide()
        self.shapeedit.setEnabled(True)
        self.shapedelete.setEnabled(True)
        return

    def shapeeditClicked(self):

        if self.ShapeList.count() > 0:
            self.shapeSave.hide()
            self.shapeUpdate.show()
            self.shapeframe.show()
            self.shapeedit.setEnabled(False)
            self.shapedelete.setEnabled(False)

            shapeText  = self.ShapeList.item(self.ShapeList.currentRow()).text()
            shapeText = shapeText.replace("{", "")
            shapeText = shapeText.replace("}", "")
            shapeData = shapeText.split(" ")
            shapeValues = shapeData[1].split(",")


            self.shapeframe.show()
            self.cube_end.setText("")
            self.cube_start.setText("")
            self.cylinder_center.setText("")
            self.cylinder_radius.setText("")
            self.cylinder_zend.setText("0")
            self.cylinder_zstart.setText("0")
            self.ellipse_center.setText("")
            self.ellipse_eccentric.setText("")
            self.ellipse_majorAxis.setText("")
            self.ellipse_rotation.setText("")
            self.sphere_center.setText("")
            self.sphere_radius.setText("")

            if shapeData[0] =="CUBE":
                self.fillCUBE.show()
                self.fillCYLINDER.hide()
                self.fillELLIPSE.hide()
                self.fillSPHERE.hide()
                self.shapeFrameTitle.setText("CUBE | "+self.pDropdown_3.itemText(int(shapeValues[0])))

                self.cube_start.setText(','.join(map(str, shapeValues[1:4])))
                self.cube_end.setText(','.join(map(str, shapeValues[4:])))

                return

            elif shapeData[0] =="CYLINDER":
                self.fillCUBE.hide()
                self.fillCYLINDER.show()
                self.fillELLIPSE.hide()
                self.fillSPHERE.hide()
                self.shapeFrameTitle.setText("CYLINDER | "+self.pDropdown_3.itemText(int(shapeValues[0])))
                self.cylinder_center.setText(','.join(map(str, shapeValues[1:3])))
                self.cylinder_zend.setText(str(shapeValues[3]))
                self.cylinder_zstart.setText(str(shapeValues[4]))
                self.cylinder_radius.setText(str(shapeValues[5]))
                return

            elif shapeData[0] =="ELLIPSE":
                self.fillCUBE.hide()
                self.fillCYLINDER.hide()
                self.fillELLIPSE.show()
                self.fillSPHERE.hide()
                self.shapeFrameTitle.setText("ELLIPSE | "+self.pDropdown_3.itemText(int(shapeValues[0])))
                self.ellipse_center.setText(','.join(map(str, shapeValues[1:3])))
                self.ellipse_majorAxis.setText(str(shapeValues[3]))
                self.ellipse_eccentric.setText(str(shapeValues[4]))
                self.ellipse_rotation.setText(str(shapeValues[5]))
                return

            elif shapeData[0] =="SPHERE":
                self.fillCUBE.hide()
                self.fillCYLINDER.hide()
                self.fillELLIPSE.hide()
                self.fillSPHERE.show()
                self.shapeFrameTitle.setText("SPHERE | "+self.pDropdown_3.itemText(int(shapeValues[0])))
                self.sphere_center.setText(','.join(map(str, shapeValues[1:4])))
                self.sphere_radius.setText(shapeValues[4])
                return


    def shapedeleteClicked(self):
        self.ShapeList.takeItem(self.ShapeList.currentRow())

    def radio_GPToggled(self):

        if self.radio_GP.isChecked():
            self.btn7.setEnabled(False)
            self.btn6.setText("Grand-Potential \n Model")
            self.frame_9GP.show()
            self.frame_9KKS.hide()
            self.frame_9CH.hide()
            self.frame_9KKS2.hide()


    def radio_CHToggled(self):

        if self.radio_CH.isChecked():
            self.btn7.setEnabled(False)
            self.btn6.setText("Cahn Hilliard\n Model")
            self.frame_9GP.hide()
            self.frame_9CH.show()
            self.frame_9KKS.hide()
            self.frame_9KKS2.hide()


    def radio_KKRToggled(self):

        if self.radio_KKR.isChecked():
            self.btn7.setEnabled(False)
            self.btn6.setText("KKS GPU CUDA\n   Model")
            self.frame_9GP.hide()
            self.frame_9CH.hide()
            self.frame_9KKS2.hide()
            self.frame_9KKS.show()

    def radio_KKS2Toggled(self):

        if self.radio_KKS2.isChecked():
            self.btn7.setEnabled(False)
            self.btn6.setText("KKS GPU OPENCL \n   Model")
            self.frame_9GP.hide()
            self.frame_9CH.hide()
            self.frame_9KKS.hide()
            self.frame_9KKS2.show()


    def GPnextClicked(self):

        if self.stackedWidgetGP.currentIndex() == 3:
            self.saveGP.show()

        if self.stackedWidgetGP.currentIndex() < 4:
            self.stackedWidgetGP.setCurrentIndex((self.stackedWidgetGP.currentIndex() +1) )
        else:
            return


    def GPpreClicked(self):
        self.saveGP.hide()
        if self.stackedWidgetGP.currentIndex() > 0:
            self.stackedWidgetGP.setCurrentIndex((self.stackedWidgetGP.currentIndex() -1)  )
        else:
            return

    def saveGPClicked(self):

        if self.saveGPChack():
            self.btn7.setEnabled(True)
            self.frame_8.hide()
            self.frame_9.hide()
            self.First_widget.hide()
            self.Second_widget.hide()
            self.Third_widget.hide()
            self.Four_widget.hide()
            self.Fifth_widget.hide()
            self.Sixth_widget.hide()
            self.Seven_widget.show()


            self.Qbox.hide()
            self.frame_11.show()


            #Btn Animation
            self.btn5.setGeometry(60, 30, 200, 60)
            self.btn6.setGeometry(260, 30, 200, 60)
            self.btn7.setGeometry(460, 20, 200, 70)


            self.btn7.setStyleSheet("background-color: rgb(64, 140, 191); border:none ;color:#fff ")
            self.btn5.setStyleSheet("background-color: rgb(238, 238, 236)")
            self.btn6.setStyleSheet("background-color: rgb(238, 238, 236)")


        else:
            return


    def saveGPChack(self):

        noP_value = self.noP.value()

        for i in range(noP_value):
            if self.tableWidgetGPA.item(i,1) is None or self.tableWidgetGPA.item(i,1).text() == '':
                self.errorGP.setText("Please fill All values of A")
                return False

        for i in range(noP_value*noP_value):
            for j in range(2,6,1):
                if self.tableWidgetGP.item(i,j) is None or self.tableWidgetGP.item(i,j).text() == '':
                    self.errorGP.setText("Please fill All values of Ceq, cfill ..")
                    return False


        if self.trackProgressGP.text() == "":
            self.errorGP.setText("Please fill Track Progress ")
            return False

        elif self.epsilonGP.text() == "":
            self.errorGP.setText("Please fill Epsilon value")
            return False

        elif self.tauGP.text() == "":
            self.errorGP.setText("Please fill tau Value")
            return False

        elif self.TauGP.text() == "":
            self.errorGP.setText("Please fill Tau values")
            return False

        elif len(self.TauGP.text().split(",")) != (noP_value * ((noP_value - 1) / 2)):
            self.errorGP.setText("Required " + str((noP_value * ((noP_value - 1) / 2))) + " values for Tau" )
            return False

        elif self.FanisotropyGP.text() == "":
            self.errorGP.setText("Please fill Function Anisotropy")
            return False

        elif self.anisotropyTypeGP.text() == "":
            self.errorGP.setText("Please fill Anisotropy Type")
            return False

        elif self.debGP.text() == "":
            self.errorGP.setText("Please fill dab values")
            return False

        elif len(self.debGP.text().split(",")) != int(noP_value * ((noP_value - 1) / 2)):
            self.errorGP.setText("Required " + str((noP_value * ((noP_value - 1) / 2))) + " values for dab" )
            return False

        elif self.funcWGP.text() == "":
            self.errorGP.setText("Please fill Functional W value")
            return False

        elif self.funcFGP.text() =="":
            self.errorGP.setText("Please fill Functional F value")
            return False


        elif len(self.gammaABCGP.text().split(",")) != int(noP_value * ((noP_value - 1)*(noP_value - 2) / 6)) and self.gammaABCGP.text() != "":
            self.errorGP.setText("Required " + str(int((noP_value * ((noP_value - 1)*(noP_value - 2) / 6)))) + " values for Gamma abc" )
            return False

        elif self.shiftJGP.text() =="" and self.shiftGP.value() == 1:
            self.errorGP.setText("Please fill Shift J value")
            return False

        elif self.equTGP.text() == "":
            self.errorGP.setText("Please fill Equilibrium Temperature")
            return False

        elif self.fillingTGP.text() =="":
            self.errorGP.setText("Please fill Filling Temperature")
            return False

        elif self.TGP.text() =="":
            self.errorGP.setText("Please fill Temperature")
            return False

        elif self.tempgradyGP.text() == "":
            self.errorGP.setText("Please fill Tempgrady values")
            return False

        elif len(self.tempgradyGP.text().split(",")) != 5:
            self.errorGP.setText("Required 5 values for Tempgrady" )
            return False

        elif self.ampNoiseGP.text() =="" and self.noiseGP.value() == 1:
            self.errorGP.setText("Please fill AMP Noise value")
            return False

        elif self.writecompGP.text() == "":
            self.errorGP.setText("Please fill Writecomposition Value")
            return False

        else:
            self.errorGP.setText("")
            return True


    def KKSnextClicked(self):

        if self.stackedWidgetKKS.currentIndex() == 0:
            self.saveKKS.show()

        if self.stackedWidgetKKS.currentIndex() < 1:
            self.stackedWidgetKKS.setCurrentIndex((self.stackedWidgetKKS.currentIndex() +1) )
        else:
            return


    def KKSpreClicked(self):
        self.saveKKS.hide()
        if self.stackedWidgetKKS.currentIndex() > 0:
            self.stackedWidgetKKS.setCurrentIndex((self.stackedWidgetKKS.currentIndex() -1)  )
        else:
            return

    def saveKKSClicked(self):

        if self.saveKKSCheck():
            self.errorKKS.setText("")
            self.btn7.setEnabled(True)
            self.frame_8.hide()
            self.frame_9.hide()
            self.First_widget.hide()
            self.Second_widget.hide()
            self.Third_widget.hide()
            self.Four_widget.hide()
            self.Fifth_widget.hide()
            self.Sixth_widget.hide()
            self.Seven_widget.show()

            self.Qbox.hide()
            self.frame_11.show()


            #Btn Animation
            self.btn5.setGeometry(60, 30, 200, 60)
            self.btn6.setGeometry(260, 30, 200, 60)
            self.btn7.setGeometry(460, 20, 200, 70)


            self.btn7.setStyleSheet("background-color: rgb(64, 140, 191); border:none ;color:#fff ")
            self.btn5.setStyleSheet("background-color: rgb(238, 238, 236)")
            self.btn6.setStyleSheet("background-color: rgb(238, 238, 236)")

        else:
            return

    def saveKKSCheck(self):

        noP_value = self.noP.value()

        for i in range(noP_value):
            if self.tableWidgetKKSF.item(i,1) is None or self.tableWidgetKKSF.item(i,1).text() == '':
                self.errorKKS.setText("Please fill All values of F")
                return False

        for i in range(noP_value*noP_value):
            if self.tableWidgetKKS.item(i,2) is None or self.tableWidgetKKS.item(i,2).text() == '':
                self.errorKKS.setText("Please fill All values of Ceq")
                return False


        if self.trackprogressKKS.text() == "":
            self.errorKKS.setText("Please fill Track Progress Size ")
            return False
        
        elif self.relaxCoeffKKS.text() == "":
            self.errorKKS.setText("Please fill relaxCoeff value")
            return False

        elif self.alphaKKS.text() == "":
            self.errorKKS.setText("Please fill Alpha value ")
            return False

        elif self.lambdaKKS.text() == "":
            self.errorKKS.setText("Please fill lambda value ")
            return False

        elif self.CKKS.text() == "":
            self.errorKKS.setText("Please fill C0 value")
            return False

        elif self.ampNoiseKKS.text() == "" and self.noiseKKS.value() == 1:
            self.errorKKS.setText("Please fill AMP Noise value")
            return False

        elif self.elastIntKKS.text() == "":
            self.errorKKS.setText("Please fill Elast INT value")
            return False

        else:
            self.errorKKS.setText("")
            return True

    def KKS2nextClicked(self):

        if self.stackedWidgetKKS2.currentIndex() == 2:
            self.saveKKS2.show()

        if self.stackedWidgetKKS2.currentIndex() < 3:
            self.stackedWidgetKKS2.setCurrentIndex((self.stackedWidgetKKS2.currentIndex() +1) )
        else:
            return


    def KKS2preClicked(self):
        self.saveKKS2.hide()
        if self.stackedWidgetKKS2.currentIndex() > 0:
            self.stackedWidgetKKS2.setCurrentIndex((self.stackedWidgetKKS2.currentIndex() -1)  )
        else:
            return

    def saveKKS2Clicked(self):

        if self.saveKKS2Check():
            self.errorKKS2.setText("")
            self.btn7.setEnabled(True)
            self.frame_8.hide()
            self.frame_9.hide()
            self.First_widget.hide()
            self.Second_widget.hide()
            self.Third_widget.hide()
            self.Four_widget.hide()
            self.Fifth_widget.hide()
            self.Sixth_widget.hide()
            self.Seven_widget.show()

            self.Qbox.hide()
            self.frame_11.show()


            #Btn Animation
            self.btn5.setGeometry(60, 30, 200, 60)
            self.btn6.setGeometry(260, 30, 200, 60)
            self.btn7.setGeometry(460, 20, 200, 70)


            self.btn7.setStyleSheet("background-color: rgb(64, 140, 191); border:none ;color:#fff ")
            self.btn5.setStyleSheet("background-color: rgb(238, 238, 236)")
            self.btn6.setStyleSheet("background-color: rgb(238, 238, 236)")

        else:
            return

    def saveKKS2Check(self):

        noP_value = self.noP.value()

        for i in range(noP_value*noP_value):
            for j in range(2,5,1):
                if self.tableWidgetKKS2.item(i,j) is None or self.tableWidgetKKS2.item(i,j).text() == '':
                    self.errorKKS2.setText("Please fill All values of Ceq, cfill.")
                    return False


        if self.trackProgressKKS2.text() == "":
            self.errorKKS2.setText("Please fill Track Progress ")
            return False

        elif self.epsilonKKS2.text() == "":
            self.errorKKS2.setText("Please fill Epsilon value")
            return False


        elif self.FanisotropyKKS2.text() == "":
            self.errorKKS2.setText("Please fill Function Anisotropy")
            return False


        elif self.debKKS2.text() == "":
            self.errorKKS2.setText("Please fill dab values")
            return False

        elif len(self.debKKS2.text().split(",")) != int(noP_value * ((noP_value - 1) / 2)):
            self.errorKKS2.setText("Required " + str((noP_value * ((noP_value - 1) / 2))) + " values for dab" )
            return False

        elif self.ampNoiseKKS2.text() == "" and self.noiseKKS2.value() == 1:
            self.errorKKS2.setText("Please fill AMP Noise value")
            return False

        elif self.tNoiseStartKKS2.text() == "":
            self.errorKKS2.setText("Please fill tNoiseStart value")
            return False

        elif self.TLKKS2.text() == "":
            self.errorKKS2.setText("Please fill T Liquidus value")
            return False

        elif self.tempGradyKKS2.text() == "":
            self.errorKKS2.setText("Please fill Tempgrady values")
            return False

        elif len(self.tempGradyKKS2.text().split(",")) != 5:
            self.errorKKS2.setText("Required 5 values for Tempgrady" )
            return False

        elif self.atrKKS2.text() == "":
            self.errorKKS2.setText("Please fill atr value")
            return False

        elif self.CLPidKKS2.text() == "":
            self.errorKKS2.setText("Please fill CL Plateform ID value")
            return False

        elif self.CLDidKKS2.text() == "":
            self.errorKKS2.setText("Please fill CL devise ID value")
            return False
        
        elif self.tdbfnameKKS2.text() == "":
            self.errorKKS2.setText("Please fill tdbfname")
            return False

        else:
            self.errorKKS2.setText("")
            return True



    def CHnextClicked(self):

        if self.stackedWidgetCH.currentIndex() == 0:
            self.saveCH.show()

        if self.stackedWidgetCH.currentIndex() < 1:
            self.stackedWidgetCH.setCurrentIndex((self.stackedWidgetCH.currentIndex() +1) )
        else:
            return


    def CHpreClicked(self):
        self.saveCH.hide()
        if self.stackedWidgetCH.currentIndex() > 0:
            self.stackedWidgetCH.setCurrentIndex((self.stackedWidgetCH.currentIndex() -1)  )
        else:
            return

    def saveCHClicked(self):

        if self.saveCHCheck():
            self.btn7.setEnabled(True)
            self.frame_8.hide()
            self.frame_9.hide()
            self.First_widget.hide()
            self.Second_widget.hide()
            self.Third_widget.hide()
            self.Four_widget.hide()
            self.Fifth_widget.hide()
            self.Sixth_widget.hide()
            self.Seven_widget.show()

            self.Qbox.hide()
            self.frame_11.show()


            #Btn Animation
            self.btn5.setGeometry(60, 30, 200, 60)
            self.btn6.setGeometry(260, 30, 200, 60)
            self.btn7.setGeometry(460, 20, 200, 70)


            self.btn7.setStyleSheet("background-color: rgb(64, 140, 191); border:none ;color:#fff ")
            self.btn5.setStyleSheet("background-color: rgb(238, 238, 236)")
            self.btn6.setStyleSheet("background-color: rgb(238, 238, 236)")

        else:
            return


    def saveCHCheck(self):

        noP_value = self.noP.value()

        for i in range(noP_value):
            if self.tableWidgetCHA.item(i,2) is None or self.tableWidgetCHA.item(i,2).text() == '':
                self.errorCH.setText("Please fill All values of Atomic Mobility")
                return False

        for i in range(noP_value*noP_value):
            for j in range(2,4,1):
                if self.tableWidgetCH.item(i,j) is None or self.tableWidgetCH.item(i,j).text() == '':
                    self.errorCH.setText("Please fill All values of Ceq, cfill.")
                    return False


        if self.trackProgressCH.text() == "":
            self.errorCH.setText("Please fill Track Progress ")
            return False

        elif self.lPhiCH.text() == "":
            self.errorCH.setText("Please fill L Phi value")
            return False

        elif len(self.lPhiCH.text().split(",")) != int(noP_value * ((noP_value - 1) / 2)):
            self.errorCH.setText("Required " + str((noP_value * ((noP_value - 1) / 2))) + " values for L Phi" )
            return False

        elif self.kappaPhiCH.text() == "":
            self.errorCH.setText("Please fill Kappa Phi value")
            return False

        elif len(self.kappaPhiCH.text().split(",")) != int(noP_value * ((noP_value - 1) / 2)):
            self.errorCH.setText("Required " + str((noP_value * ((noP_value - 1) / 2))) + " values for Kappa Phi" )
            return False

        elif self.kappaCCH.text() == "":
            self.errorCH.setText("Please fill Kappa C value")
            return False

        elif len(self.kappaCCH.text().split(",")) != int(noP_value * ((noP_value - 1) / 2)):
            self.errorCH.setText("Required " + str((noP_value * ((noP_value - 1) / 2))) + " values for Kappa C" )
            return False

        elif self.afmCH.text() == "":
            self.errorCH.setText("Please fill A fm value")
            return False

        elif self.bfpCH.text() == "":
            self.errorCH.setText("Please fill B fm value")
            return False


        elif self.tdbfnameCH.text() == "" and self.tdbflagCH.value() == 1:
            self.errorCH.setText("Please fill tdbfname")
            return False

        else:
            self.errorCH.setText("")
            return True

    def updatetdbflag(self):
        if self.tdbflagCH.value() ==0:
            self.tdbfnameCH.setText("")
            self.tdbfnameCH.setEnabled(False)
        elif self.tdbflagCH.value() ==1:
            self.tdbfnameCH.setEnabled(True)

    def tableItemClickedCHA(self):
        if self.tableWidgetCHA.selectedItems()[0].text()  =="DM":
            self.tableWidgetCHA.selectedItems()[0].setText("FM")

        elif self.tableWidgetCHA.selectedItems()[0].text()  =="FM":
            self.tableWidgetCHA.selectedItems()[0].setText("DM")

        else:
            return


    def clickedfinish(self):  ##code for finish btn operation. it firstly varifies the data then generate file

        dimesion = self.dim.value()

        if self.mesh_x.text() != "":
            mesh_X = self.mesh_x.text()
        else:
            self.finish_error.setText("Please fill Mesh-X Value")
            return

        if self.mesh_y.text() != "":
            mesh_Y = self.mesh_y.text()
        else:
            self.finish_error.setText("Please fill Mesh-Y Value")
            return

        if self.mesh_z.text() != "":
            mesh_Z = self.mesh_z.text()
        else:
            self.finish_error.setText("Please fill Mesh-Z Value")
            return


        if self.dx.text() !="":
            Dx = self.dx.text()
        else:
            self.finish_error.setText("Please fill dx Value")
            return

        if self.dy.text() !="":
            Dy = self.dy.text()
        else:
            self.finish_error.setText("Please fill dy Value")
            return

        if self.dz.text() !="":
            Dz = self.dz.text()
        else:
            self.finish_error.setText("Please fill dz Value")
            return

        if self.dt.text() !="":
            Dt = self.dt.text()
        else:
            self.finish_error.setText("Please fill dt Value")
            return


        NoP = self.noP.value()
        NoC = self.noC.value()

        if self.timeSteps.text() !="":
            TimeSteps = self.timeSteps.text()
        else:
            self.finish_error.setText("Please fill TimeSteps Value")
            return

        if self.saveAt.text() !="":
            saveAt = self.saveAt.text()
        else:
            self.finish_error.setText("Please fill SaveAt Value")
            return

        if self.Nsmooth.text() !="":
            Nsmooth = self.Nsmooth.text()
        else:
            self.finish_error.setText("Please fill Nsmooth Value")
            return
        
        RESTART = self.reStart.value()

        if self.startTime.text() !="":
            STARTTIME = self.startTime.text()
        else:
            self.finish_error.setText("Please fill Start Time")
            return
        
        NumWORKERS = self.numWorkers.text()

        COMPONENTS_name = self.ctext.toPlainText().splitlines()
        if len( COMPONENTS_name) != NoC:
            self.finish_error.setText("Required " + str(NoC) + " Components Names ")
            return
        else:
            COMPONENTS =COMPONENTS_name[0]
            for j in range(1,len(COMPONENTS_name),1):
                COMPONENTS = COMPONENTS + "," + COMPONENTS_name[j]


        PHASES_name = self.ptext.toPlainText().splitlines()
        if len(PHASES_name) != NoP:
            self.finish_error.setText("Required " + str(NoP) + " Phases Names ")
            return
        else:
            PHASES =PHASES_name[0]
            for k in range(1,len(PHASES_name),1):
                PHASES = PHASES + "," +PHASES_name[k]


        GAMMA_val = self.gammaInput.text().split(",")
        if len(GAMMA_val) != int(NoP*((NoP - 1)/2)) or self.gammaInput.text() == "":
            self.finish_error.setText("Required " + str(int(NoP*((NoP - 1)/2))) + " Gamma Values ")
            return
        else:
            GAMMA = self.gammaInput.text()

        if self.R_Value.text() !="":
            R = self.R_Value.text()
        else:
            self.finish_error.setText("Please fill R Value")
            return
        
        if self.V_Value.text() !="":
            V = self.V_Value.text()
        else:
            self.finish_error.setText("Please fill V Value")
            return
        

        DIFFUSIVITY = [""]*NoP
        EIGEN_STRAIN =[""]*NoP
        VOIGT = [""]*NoP

        for i in range(NoP):
            if self.Diffusivity[i] != "" :
                diff = self.Diffusivity[i].split(",")
                if self.DiffusivityType[i] ==0 and len(diff) != NoP*NoP:
                    self.finish_error.setText("Required " + str(NoP*NoP) + "Diffusivity Values for phase " + PHASES_name[i])
                    return
                elif self.DiffusivityType[i] == 1 and len(diff) != NoP:
                    self.finish_error.setText("Required " + str(NoP) + "Diffusivity Values for phase " + PHASES_name[i])
                    return

                else:
                    DIFFUSIVITY[i] = "{" + str(self.DiffusivityType[i]) + "," + str(i) +"," + str(self.Diffusivity[i])+"};\n"



            if self.eigenStrain[i] == "" or len(self.eigenStrain[i].split(",")) !=6:
                self.finish_error.setText("Required 6 Eigenstrain Values for phase " + PHASES_name[i])
                return
            else:
                EIGEN_STRAIN[i] = "{"+str(i) + "," + str(self.eigenStrain[i]) +"};\n"

            if self.elasticConstant[i] != "":

                elasticCON = self.elasticConstant[i].split(",")
                elasticTP = ""

                if self.elasticType[i] == "0" and len(elasticCON) !=3:
                    self.finish_error.setText("Required 3 elastic Constant Values for phase " + PHASES_name[i])
                    return

                elif self.elasticType[i] == "0" and len(elasticCON) ==3:

                    elasticTP ="VOIGT_ISOTROPIC"

                elif self.elasticType[i] == "1" and len(elasticCON) !=3:
                    self.finish_error.setText("Required 3 elastic Constant Values for phase " + PHASES_name[i])
                    return

                elif self.elasticType[i] == "1" and len(elasticCON) ==3:
                    elasticTP = "VOIGT_CUBIC"

                elif self.elasticType[i] == "2" and len(elasticCON) !=6:
                    self.finish_error.setText("Required 6 elastic Constant Values for phase " + PHASES_name[i])
                    return

                elif self.elasticType[i] == "2" and len(elasticCON) ==6:
                    elasticTP ="VOIGT_TETRAGONAL"

                VOIGT[i] = elasticTP + " = {" + str(i) +","+  str(self.elasticConstant[i]) + "};\n"

        #checking infile filling file

        if self.infile.text() == "":
            self.finish_error.setText("Please fill Infile Name")
            return

        if self.filling.text() == "":
            self.finish_error.setText("Please fill filling Name")
            return


        ## WRITING ON FILE

        dlg = QtWidgets.QFileDialog()
        dlg.setFileMode(QtWidgets.QFileDialog.Directory)
        if dlg.exec_():
            self.runDir =  ''.join(dlg.selectedFiles())
            infilename =  self.runDir + "/" + self.infile.text()
            fillingname = self.runDir + "/" + self.filling.text()

        else:
            self.finish_error.setText("Error occure while selecting directory. Do not select root directory.")
            return

        f = open(infilename, "w")
        f.write("##Geometrical dimensions of the simulation domain\n"
                "DIMENSION = " + str(dimesion) + ";\n"
                "MESH_X = " + str(mesh_X) + ";\n"
                "MESH_Y = " + str(mesh_Y) + ";\n"
                "MESH_Z = " + str(mesh_Z) + ";\n"
                "##Discretization, space and time\n"
                "DELTA_X = " + str(Dx) + ";\n"
                "DELTA_Y = " + str(Dy) + ";\n"
                "DELTA_Z = " + str(Dz) + ";\n"
                "DELTA_t = " + str(Dt) + ";\n"
                "##Number of phases and composition\n"
                "NUMPHASES = " + str(NoP) + ";\n"
                "NUMCOMPONENTS = " + str(NoC) + ";\n"
                "#Running and saving information\n"
                "NTIMESTEPS = " + str(TimeSteps) + ";\n"
                "NSMOOTH = " + str(Nsmooth) + ";\n"
                "SAVET = " + str(saveAt) + ";\n"
                "RESTART = " + str(RESTART) + ";\n"
                "STARTTIME = " + str(STARTTIME) + ";\n"
                "numworkers = " + str(NumWORKERS) + ";\n"
                "## Component and Phase names\n"
                "COMPONENTS = {" + COMPONENTS +"};\n"
                "PHASES = {" + PHASES +"};\n"
                "##Material properties\n"
                "GAMMA = {"+ str(GAMMA) +"};\n"
                "R = " + R +";\n"
                "V = " + V +";\n"
                )

        for i in range(len(DIFFUSIVITY)):
            f.write("DIFFUSIVITY = " + DIFFUSIVITY[i] )

        for i in range(len(EIGEN_STRAIN)):
            f.write("EIGEN_STRAIN = " + EIGEN_STRAIN[i] )

        for i in range(len(VOIGT)):
            f.write( VOIGT[i] )


        #Boundary Conditions
        f.write("##Boundary conditions\n")
        if self.Bcnd[0] =="":
            self.finish_error.setText("Required Boundary Conditions Values for phi ")

        else:
            f.write("BOUNDARY = {phi," + self.Bcnd[0] + ",0,0};\n")

        if self.Bcnd[1] =="" and self.Bcnd[2] =="":
            self.finish_error.setText("Required Boundary Conditions Values for mu ")

        else:
            f.write("BOUNDARY = {mu," + self.Bcnd[1] + ",0,0};\n")

        if self.Bcnd[2] !="":
            f.write("BOUNDARY = {c," + self.Bcnd[2] + ",0,0};\n")

        if self.Bcnd[3] =="":
            self.finish_error.setText("Required Boundary Conditions Values for T ")

        else:
            f.write("BOUNDARY = {T," + self.Bcnd[3] + ",0,0};\n")

        #BOUNDARY VALUE

        if self.BconV[0] =="":
            self.finish_error.setText("Required Boundary Values for phi ")

        else:
            f.write("BOUNDARY_VALUE = {phi," + self.BconV[0] + ",0,0};\n")

        if self.BconV[1] =="" and self.BconV[2] =="":
            self.finish_error.setText("Required Boundary Values for mu ")

        else:
            f.write("BOUNDARY_VALUE = {mu," + self.BconV[1] + ",0,0};\n")

        if self.BconV[2] !="":
            f.write("BOUNDARY_VALUE = {c," + self.BconV[2] + ",0,0};\n")

        if self.BconV[3] =="":
            self.finish_error.setText("Required Boundary Values for T ")

        else:
            f.write("BOUNDARY_VALUE = {T," + self.BconV[3] + ",0,0};\n")

        #MODEL SPECIFIC PARAMETER
        if self.radio_GP.isChecked():

            if self.saveGPChack():
                f.write("##Model-specific parameters: Grand-potential model\n")

                if self.thermalYGP.isChecked():
                    ISOTHERMALVvalue = 1
                elif self.thermalNGP.isChecked():
                    ISOTHERMALVvalue = 0

                f.write("ISOTHERMAL = " + str(ISOTHERMALVvalue) + ";\n")

                if self.simTypeGP.currentIndex() == 0:
                    f.write("BINARY = 1;\nTERNARY = 0;\nDILUTE = 0;\n")
                elif self.simTypeGP.currentIndex() == 1:
                    f.write("BINARY = 0;\nTERNARY = 1;\nDILUTE = 0;\n")
                elif self.simTypeGP.currentIndex() == 2:
                    f.write("BINARY = 0;\nTERNARY = 0;\nDILUTE = 1;\n")

                f.write("T = " + self.TGP.text() + ";\n"
                        "WRITEFORMAT = "+self.writeFormatGP.currentText()+";\n"
                        "WRITEHDF5 = " + str(self.writehdfGP.value()) +";\n"
                        "TRACK_PROGRESS = " + self.trackProgressGP.text()+";\n"
                        "epsilon = " + self.epsilonGP.text()+";\n"
                        "tau = " + self.tauGP.text()+";\n"
                        "Tau = {" + self.TauGP.text()+"};\n"
                        "Function_anisotropy = " + self.FanisotropyGP.text()+";\n"
                        "Anisotropy_type = " + self.anisotropyTypeGP.text()+";\n"
                        "dab = {" + self.debGP.text()+"};\n"
                        "Function_W = " + self.funcWGP.text()+";\n"
                        "Gamma_abc = {" + self.gammaABCGP.text()+"};\n"
                        "Shift = " + str(self.shiftGP.value())+";\n"
                        "Shiftj = " + self.shiftJGP.text()+";\n"
                        "Writecomposition = " + self.writecompGP.text()+";\n"
                        "Noise_phasefield = " + str(self.noiseGP.value()) +";\n"
                        "Amp_Noise_Phase = " + self.ampNoiseGP.text()+";\n"
                        "Equilibrium_temperature = " + self.equTGP.text()+";\n"
                        "Filling_temperature = " + self.fillingTGP.text()+";\n"
                        "Tempgrady = {" + self.tempgradyGP.text()+"};\n"
                        "Function_F = " + self.funcFGP.text()+";\n")

                dummycount =0

                for i in range(NoP):
                    for j in range(NoP):
                        if j!=i and j>i:
                            f.write("Rotation_matrix = {" +  self.tableWidgetGP.item(dummycount,0).text() + ","+ self.tableWidgetGP.item(dummycount,1).text() + "," + self.tableWidgetGP.item(dummycount,5).text() + "};\n")
                        dummycount = dummycount+1

                for i in range(NoP):
                    f.write("A = {" + str(i) +"," +self.tableWidgetGPA.item(i,1).text()+"};\n")

                for i in range(NoP*NoP):
                    if self.tableWidgetGP.item(i,2).text() !="-":
                        f.write("ceq = {" +  self.tableWidgetGP.item(i,0).text() + ","+ self.tableWidgetGP.item(i,1).text() + "," + self.tableWidgetGP.item(i,2).text() + "};\n")

                for i in range(NoP*NoP):
                    if self.tableWidgetGP.item(i,3).text() !="-":
                        f.write("cfill = {" +  self.tableWidgetGP.item(i,0).text() + ","+ self.tableWidgetGP.item(i,1).text() + "," + self.tableWidgetGP.item(i,3).text() + "};\n")

                for i in range(NoP*NoP):
                    if self.tableWidgetGP.item(i,4).text() !="-":
                        f.write("slopes = {" +  self.tableWidgetGP.item(i,0).text() + ","+ self.tableWidgetGP.item(i,1).text() + "," + self.tableWidgetGP.item(i,4).text() + "};\n")

            else:
                self.finish_error.setText("Fill All required Model Specific Parameter")
                return


        elif self.radio_KKR.isChecked():

            if self.saveKKSCheck():

                f.write("##Model-specific parameters: KKS FFT GPU \n")
                f.write("WRITEFORMAT = "+self.writeFormatKKS.currentText()+";\n"
                        "TRACK_PROGRESS = " + self.trackprogressKKS.text()+";\n"
                        "Noise_phasefield = " + str(self.noiseKKS.value()) +";\n"
                        "Amp_Noise_Phase = " + self.ampNoiseKKS.text()+";\n"
                        "relax_coeff = " + self.relaxCoeffKKS.text()+";\n"
                        "c0 = " + self.CKKS.text()+";\n"
                        "alpha = " + self.alphaKKS.text()+";\n"
                        "lambda = " + self.lambdaKKS.text()+";\n"
                        "ELAST_INT = " + self.elastIntKKS.text()+";\n"
                    )

                for i in range(NoP):
                    f.write("f0 = {" +  self.tableWidgetKKSF.item(i,0).text() + ","+ self.tableWidgetKKSF.item(i,1).text() + "};\n")

                for i in range(NoP*NoP):
                    if self.tableWidgetKKS.item(i,2).text() !="-":
                        f.write("ceq = {" +  self.tableWidgetKKS.item(i,0).text() + ","+ self.tableWidgetKKS.item(i,1).text() + "," + self.tableWidgetKKS.item(i,2).text() + "};\n")


        elif self.radio_KKS2.isChecked():

            if self.saveKKS2Check():

                f.write("##Model-specific parameters: Kim model\n")

                if self.thermalYKKS2.isChecked():
                    ISOTHERMALvalue = 1
                elif self.thermalNKKS2.isChecked():
                    ISOTHERMALvalue = 0

                f.write("ISOTHERMAL = " + str(ISOTHERMALvalue) + ";\n")

                if self.simTypeKKS2.currentIndex() == 0:
                    f.write("BINARY = 1;\nTERNARY = 0;\nDILUTE = 0;\n")
                elif self.simTypeKKS2.currentIndex() == 1:
                    f.write("BINARY = 0;\nTERNARY = 1;\nDILUTE = 0;\n")
                elif self.simTypeKKS2.currentIndex() == 2:
                    f.write("BINARY = 0;\nTERNARY = 0;\nDILUTE = 1;\n")

                f.write("WRITEFORMAT = "+self.writeFormatKKS2.currentText()+";\n"
                        "TRACK_PROGRESS = " + self.trackProgressKKS2.text()+";\n"
                        "epsilon = " + self.epsilonKKS2.text()+";\n"
                        "Function_anisotropy = " + self.FanisotropyKKS2.text()+";\n"
                        "dab = {" + self.debKKS2.text()+"};\n"
                        "Noise_phasefield = " + str(self.noiseKKS2.value()) +";\n"
                        "Amp_Noise_Phase = " + self.ampNoiseKKS2.text()+";\n"
                        "Tempgrady = {" + self.tempGradyKKS2.text()+"};\n"
                        "tNoiseStart = " + self.tNoiseStartKKS2.text()+";\n"
                        "TLiquidus = " + self.TLKKS2.text()+";\n"

                        "atr = " + self.atrKKS2.text()+";\n"
                        "CLplatformID = " + self.CLPidKKS2.text()+";\n"
                        "CLdeviceID = " + self.CLDidKKS2.text()+";\n"
                        "tdbfname = " + self.tdbfnameKKS2.text()+";\n"
                        )
                if self.temperatureKKS2.text() != "":
                    f.write("temperature = " + self.temperatureKKS2.text()+";\n")

                for i in range(NoP*NoP):
                    if self.tableWidgetKKS2.item(i,2).text() !="-":
                        f.write("ceq = {" +  self.tableWidgetKKS2.item(i,0).text() + ","+ self.tableWidgetKKS2.item(i,1).text() + "," + self.tableWidgetKKS2.item(i,2).text() + "};\n")

                for i in range(NoP*NoP):
                    if self.tableWidgetKKS2.item(i,3).text() !="-":
                        f.write("cfill = {" +  self.tableWidgetKKS2.item(i,0).text() + ","+ self.tableWidgetKKS2.item(i,1).text() + "," + self.tableWidgetKKS2.item(i,3).text() + "};\n")

                dummycount =0

                for i in range(NoP):
                    for j in range(NoP):
                        if j!=i and j>i:
                            f.write("Rotation_matrix = {" +  self.tableWidgetKKS2.item(dummycount,0).text() + ","+ self.tableWidgetKKS2.item(dummycount,1).text() + "," + self.tableWidgetKKS2.item(dummycount,4).text() + "};\n")
                        dummycount = dummycount+1


        elif self.radio_CH.isChecked():

            if self.saveCHCheck():
                f.write("##Model-specific parameters: Preipitate growth (FFT) \n")
                f.write("WRITEFORMAT = "+self.writeFormatCH.currentText()+";\n"
                        "TRACK_PROGRESS = " + self.trackProgressCH.text()+";\n"
                        "L_phi = {" + self.lPhiCH.text()+"};\n"
                        "Kappa_phi = {" + self.kappaPhiCH.text()+"};\n"
                        "Kappa_c = {" + self.kappaCCH.text()+"};\n"
                        "A_fm  = {" + self.afmCH.text() +"};\n"
                        "B_fp  = {" + self.bfpCH.text()+"};\n"
                        "spinodal = " + str(self.spinodalCH.value())+";\n"
                        "tdbflag = " + str(self.tdbflagCH.value())+";\n")

                if self.tdbflagCH.value() == 1:
                    f.write("tdbfname = " + self.tdbfnameCH.text()+";\n")

                for i in range(NoP):

                    if self.tableWidgetCHA.item(i,1).text() == "FM":
                        matrix_CHA = "0"
                    else:
                        matrix_CHA = "1"
                    f.write("AtomicMobility = {" + matrix_CHA + ","+ self.tableWidgetCHA.item(i,0).text() + "," + self.tableWidgetCHA.item(i,2).text() + "};\n")

                for i in range(NoP*NoP):
                    if self.tableWidgetCH.item(i,2).text() !="-":
                        f.write("ceq = {" +  self.tableWidgetCH.item(i,0).text() + ","+ self.tableWidgetCH.item(i,1).text() + "," + self.tableWidgetCH.item(i,2).text() + "};\n")


                for i in range(NoP*NoP):
                    if self.tableWidgetCH.item(i,3).text() !="-":
                        f.write("cfill = {" +  self.tableWidgetCH.item(i,0).text() + ","+ self.tableWidgetCH.item(i,1).text() + "," + self.tableWidgetCH.item(i,3).text() + "};\n")


            else:
                self.finish_error.setText("Fill All required Model Specific Parameter")
                return


        f.close()  ## closing infile writer


        ##writing filling file
        if self.ShapeList.count() > 0:
            f = open(fillingname, "w")

            for i in range(self.ShapeList.count()):

                shapeText  = self.ShapeList.item(i).text()
                shapeData = shapeText.split(" ")
                f.write( "FILL"+shapeData[0] + " = " + shapeData[1] + ";\n")

            f.close()
            writing_file_msg  = "\nSucessfully Created Input and Filling files as following :-\n\n               1) Input file saved as "+ self.infile.text()+"                    \n               2) Filing File saved as "+self.filling.text()+"              \n"
        else:
            writing_file_msg  = "\nSucessfully Created Input file :-\n\n  - Input file saved as "+ self.infile.text()+"                    \n\nUnable to create filling file. Error - Empty Filiing Data .\n"

        self.finish_error.setText("")

        Submitmsg = QMessageBox()
        Submitmsg.setWindowTitle("File Created")
        Submitmsg.setText(writing_file_msg)
        Submitmsg.exec_()

        self.runBtn.setEnabled(True)
        self.preview.setEnabled(True)

    def clickedpreview(self):
        if os.path.isdir(self.runDir + "/DATA/"):  ##checking data file status

            if os.path.isfile("/opt/paraviewopenfoam56/bin/paraview"):  ##checking paraview installation status
                list_of_files = glob.glob(self.runDir + "/DATA/"+ self.output.text() +"*.*")
                latest_file = max(list_of_files, key=os.path.getctime)
                paraviewcmd = "gnome-terminal -e 'bash -c \"/opt/paraviewopenfoam56/bin/paraview " +latest_file +"; bash\" '"
                os.system(paraviewcmd)
            elif os.path.isfile(os.path.expanduser("~/MicroSim/.Paraview")): ## Checking for paraview saved path
                readPath = open(os.path.expanduser('~/MicroSim/.Paraview'), "r")
                readPathParaview = readPath.read().replace("\n", "")
                list_of_files = glob.glob(self.runDir + "/DATA/"+ self.output.text() +"*.*")
                latest_file = max(list_of_files, key=os.path.getctime)
                paraviewcmd = "gnome-terminal -e 'bash -c \"" + readPathParaview +" " +latest_file +"; bash\" '"
                os.system(paraviewcmd)

            else:
                self.paraviewError.show()
        else:
            self.finish_error.setText("Sorry, DATA directory not found.")
            
            
    def paraviewErrorCloseClicked(self):
        self.paraviewError.hide()

    def paraviewBrowseClicked(self):

        ## WRITING ON FILE
        dlgParaview = QtWidgets.QFileDialog()
        dlgParaview.setFileMode(QtWidgets.QFileDialog.AnyFile)
        if dlgParaview.exec_():
            self.paraviewDir =  ''.join(dlgParaview.selectedFiles())
            self.paraviewPath.setText(self.paraviewDir)


        else:
            self.paraviewErrorLine.setText("Error occure while selecting directory.")

        return
    
    def paraviewOpenClicked(self):

        if self.paraviewPath.text() == "":
            self.paraviewErrorLine.setText("Error : Please select a path")
        else :
            HomePathparaview = os.path.expanduser("~/MicroSim/.Paraview")
            paraviewFileDir = open(HomePathparaview, "w")
            paraviewFileDir.write(self.paraviewPath.text())
            paraviewFileDir.close()
            list_of_files = glob.glob(self.runDir + "/DATA/"+ self.output.text() +"*.*")
            latest_file = max(list_of_files, key=os.path.getctime)
            paraviewcmd = "gnome-terminal -e 'bash -c \"" + self.paraviewPath.text() +" " +latest_file +"; bash\" '"
            os.system(paraviewcmd)
            
        return
    
            
    def clickedrunBtn(self):
        if self.output.text() == "":
            self.finish_error.setText("Please fill output file name")
            return
        else:
            self.finish_error.setText("")


        if os.path.isfile(self.runDir + "/" + self.infile.text()):  ##checking Infile Location
            pass
        else:
            self.finish_error.setText("Sorry, " + self.infile.text() + " not found." )
            return

        if os.path.isfile(self.runDir + "/" + self.filling.text()):  ##checking Infile Location
            pass
        else:
            self.finish_error.setText("Sorry, " + self.filling.text() + " file not found." )
            return

        if self.radio_GP.isChecked():
            

            commandLine ="cd ~/MicroSim/Grand_potential_Finite_difference_2D_serial/ ;make clean;make; cp microsim_gp ~/MicroSim/bin/;cd " + self.runDir + ";~/MicroSim/bin/microsim_gp "  +self.infile.text()+" "+self.filling.text()+" "+self.output.text()
            os.system("gnome-terminal -e 'bash -c  \""+commandLine+";bash\"'")
        
        elif self.radio_KKR.isChecked():
            commandLine ="cd " + self.runDir +";~/kks.out " +self.infile.text()+" "+self.filling.text()+" "+self.output.text()
            os.system("gnome-terminal -e 'bash -c \""+commandLine+";bash\"'")

        elif self.radio_KKS2.isChecked():
            commandLine ="cd ~/MicroSim/KKS_OpenCl/ ;make; cp microsim_kks_opencl ~/MicroSim/bin/;cd " + self.runDir +";~/MicroSim/bin/microsim_kks_opencl " +self.infile.text()+" "+self.filling.text()+" "+self.output.text()
            os.system("gnome-terminal -e 'bash -c \""+commandLine+";bash\"'")

        elif self.radio_CH.isChecked():
            commandLine ="cd ~/MicroSim/Cahn_Hilliard_FFT_2D/ ;make; cp microsim_ch_fft ~/MicroSim/bin/;cd " + self.runDir +";~/MicroSim/bin/microsim_ch_fft " +self.infile.text()+" "+self.filling.text()+" "+self.output.text()
            os.system("gnome-terminal -e 'bash -c \""+commandLine+";bash\"'")


    def startNewClicked(self):
        self.StartFrame.hide()

    def ReadfromFile(self):
        if os.path.exists(self.fileLabel.text()):
            try:
                fileDir = open(self.fileLabel.text(), 'r')
                fileLines = fileDir.readlines()
                self.StartFrame.hide()
                self.ShapeFlag = 1
                self.gpFlag = [0]*27
                self.chFlag = [0]*26
                self.kksFlag = [0]*38
                self.kks2Flag = [0]*45
                for i in fileLines:

                    if "#" in i:
                        pass
                    elif "=" in i:
                        entries = i.split("=")
                        entries[1] = entries[1].replace(" ", "")
                        entries[1] = entries[1].replace(";", "")
                        entries[1] = entries[1].replace("\n", "")
                        if self.model_GP.isChecked():
                            self.fillEntryGP(entries[0].replace(" ", ""),entries[1] )
                        elif self.model_CH.isChecked():
                            self.fillEntryCH(entries[0].replace(" ", ""),entries[1] )
                        elif self.model_KKS.isChecked():
                            self.fillEntryKKS(entries[0].replace(" ", ""),entries[1] )
                        elif self.model_KKS2.isChecked():
                            self.fillEntryKKS2(entries[0].replace(" ", ""),entries[1] )

                #print(self.gpFlag)
                if self.model_GP.isChecked():
                    gpVariables =["DIMENSION", "MESH_X" ,"MESH_Y", "MESH_Z", "DELTA_X" ,"DELTA_Y", "DELTA_Z", "DELTA_t", "NUMPHASES", "NUMCOMPONENTS", "NTIMESTEPS", "NSMOOTH", "SAVET", "COMPONENTS", "PHASES", "GAMMA", "DIFFUSIVITY", "R", "V", "EIGEN_STRAIN", "Elastic Constant","BOUNDARY Phi","BOUNDARY mu/c","BOUNDARY T","BOUNDARY_VALUE Phi","BOUNDARY_VALUE mu/c","BOUNDARY_VALUE T"]
                    gpmsgFlag =0
                    gperror = "Oops ! we have noticed some missing parameters in your Infile\n"
                    for i in range(27):
                        if self.gpFlag[i] == 0:
                            gperror = gperror + "\n ("+str(gpmsgFlag+1) + ") " + gpVariables[i]
                            gpmsgFlag = gpmsgFlag +1
                    self.fillGPCheck()
                    if len(self.errorListGP) >0 or gpmsgFlag != 0:
                        GPmsg = QMessageBox()
                        GPmsg.setWindowTitle("Import error")
                        for n in range(len(self.errorListGP)):
                            gperror = gperror + "\n ("+str(n+1+gpmsgFlag) + ") " + self.errorListGP[n]
                        GPmsg.setText(gperror + "\n")
                        GPmsg.exec_()
                    
                if self.model_CH.isChecked():
                    chVariables =["DIMENSION", "MESH_X" ,"MESH_Y", "MESH_Z", "DELTA_X" ,"DELTA_Y", "DELTA_Z", "DELTA_t", "NUMPHASES", "NUMCOMPONENTS", "NTIMESTEPS", "NSMOOTH", "SAVET", "COMPONENTS", "PHASES", "R", "V", "WRITEFORMAT", "TRACK_PROGRESS", "AtomicMobility", "L_phi", "Kappa_phi" "Kappa_c", "A_fm", "B_fp", "ceq","cfill" ]
                    chmsgFlag =0
                    cherror = "Oops ! we have noticed some missing parameters in your Infile\n"
                    for i in range(26):
                        if self.chFlag[i] == 0:
                            cherror = cherror + "\n ("+str(chmsgFlag+1) + ") " + chVariables[i]
                            chmsgFlag = chmsgFlag +1
                    if chmsgFlag != 0:
                        CHmsg = QMessageBox()
                        CHmsg.setWindowTitle("Import error")
                        CHmsg.setText(cherror + "\n")
                        CHmsg.exec_()

                if self.model_KKS.isChecked():
                    kksVariables =["DIMENSION", "MESH_X" ,"MESH_Y", "MESH_Z", "DELTA_X" ,"DELTA_Y", "DELTA_Z", "DELTA_t", "NUMPHASES", "NUMCOMPONENTS", "NTIMESTEPS", "NSMOOTH", "SAVET", "COMPONENTS", "PHASES", "GAMMA", "DIFFUSIVITY", "R", "V", "EIGEN_STRAIN", "Elastic Constant","BOUNDARY Phi","BOUNDARY mu/c","BOUNDARY T","BOUNDARY_VALUE Phi","BOUNDARY_VALUE mu/c","BOUNDARY_VALUE T"," WRITEFORMAT", "TRACK_PROGRESS", "ELAST_INT","relax_coeff" ,"c0", "alpha", "lambda", "f0", "Noise_phasefield", "Amp_Noise_Phase", "ceq"]
                    kksmsgFlag =0
                    kkserror = "Oops ! we have noticed some missing parameters in your Infile\n"
                    for i in range(38):
                        if self.kksFlag[i] == 0:
                            kkserror = kkserror + "\n ("+str(kksmsgFlag+1) + ") " + kksVariables[i]
                            kksmsgFlag = kksmsgFlag +1
                    if kksmsgFlag != 0:
                        KKSmsg = QMessageBox()
                        KKSmsg.setWindowTitle("Import error")
                        KKSmsg.setText(kkserror + "\n")
                        KKSmsg.exec_()

                if self.model_KKS2.isChecked():
                    kks2Variables =["DIMENSION", "MESH_X" ,"MESH_Y", "MESH_Z", "DELTA_X" ,"DELTA_Y", "DELTA_Z", "DELTA_t", "NUMPHASES", "NUMCOMPONENTS", "NTIMESTEPS", "NSMOOTH", "SAVET", "COMPONENTS", "PHASES", "GAMMA", "DIFFUSIVITY", "R", "V", "BOUNDARY Phi","BOUNDARY mu/c","BOUNDARY T","BOUNDARY_VALUE Phi","BOUNDARY_VALUE mu/c","BOUNDARY_VALUE T", "ISOTHERMAL", "BINARY/TERNARY/DILUTE", "WRITEFORMAT", "TRACK_PROGRESS", "epsilon", "Function_anisotropy",  "dab", "temperature", "Noise_phasefield", "Amp_Noise_Phase", "Tempgrady", "tNoiseStart", "TLiquidus", "atr", "CLplatformID", "CLdeviceID", "tdbfname", "ceq", "cfill", "Rotation_matrix"]
                    kks2msgFlag =0
                    kks2error = "Oops ! we have noticed some missing parameters in your Infile\n"
                    for i in range(45):
                        if self.kks2Flag[i] == 0:
                            kks2error = kks2error + "\n ("+str(kks2msgFlag+1) + ") " + kks2Variables[i]
                            kks2msgFlag = kks2msgFlag +1
                    if kks2msgFlag != 0:
                        KKS2msg = QMessageBox()
                        KKS2msg.setWindowTitle("Import error")
                        KKS2msg.setText(kks2error + "\n")
                        KKS2msg.exec_()
                        
                        

                self.sideBtn2.setGeometry(0,180,220,60)
                self.sideBtn2.setStyleSheet('background-color: rgb(171, 196, 223);font: 10pt "Ubuntu";')
                self.sideBtn2.setEnabled(True)

                self.sideBtn3.setGeometry(0,240,220,60)
                self.sideBtn3.setStyleSheet('background-color: rgb(171, 196, 223);font: 10pt "Ubuntu";')
                self.sideBtn3.setEnabled(True)

                self.sideBtn4.setGeometry(0,300,220,60)
                self.sideBtn4.setStyleSheet('background-color: rgb(171, 196, 223);font: 10pt "Ubuntu";')
                self.sideBtn4.setEnabled(True)

                self.sideBtn5.setGeometry(0,360,220,60)
                self.sideBtn5.setStyleSheet('background-color: rgb(171, 196, 223);font: 10pt "Ubuntu";')
                self.sideBtn5.setEnabled(True)

                self.sideBtn6.setGeometry(0,420,220,60)
                self.sideBtn6.setStyleSheet('background-color: rgb(171, 196, 223);font: 10pt "Ubuntu";')
                self.sideBtn6.setEnabled(True)

                self.sideBtn7.setGeometry(0,480,220,60)
                self.sideBtn7.setStyleSheet('background-color: rgb(171, 196, 223);font: 10pt "Ubuntu";')
                self.sideBtn7.setEnabled(True)

            except IOError:
                print("could not read")

            except UnicodeDecodeError:
                print("could not read")

    def fillEntryGP(self,entryname, entryvalue):

        if entryname == "DIMENSION":
            self.dim.setValue(int(entryvalue))
            self.gpFlag[0] = 1
            return

        elif entryname == "MESH_X":
            self.mesh_x.setText(entryvalue)
            self.gpFlag[1] = 1
            return

        elif entryname == "MESH_Y":
            self.mesh_y.setText(entryvalue)
            self.gpFlag[2] = 1
            return

        elif entryname == "MESH_Z":
            self.mesh_z.setText(entryvalue)
            self.gpFlag[3] = 1
            return

        elif entryname == "DELTA_X":
            self.dx.setText(entryvalue)
            self.gpFlag[4] = 1
            return

        elif entryname == "DELTA_Y":
            self.dy.setText(entryvalue)
            self.gpFlag[5] = 1
            return

        elif entryname == "DELTA_Z":
            self.dz.setText(entryvalue)
            self.gpFlag[6] = 1
            return

        elif entryname == "DELTA_t":
            self.dt.setText(entryvalue)
            self.gpFlag[7] = 1
            return

        elif entryname == "NUMPHASES":
            self.noP.setValue(int(entryvalue))
            self.gpFlag[8] = 1
            return
            #self.updateNoP()

        elif entryname == "NUMCOMPONENTS":
            self.noC.setValue(int(entryvalue))
            self.gpFlag[9] = 1
            return
            #self.updateNoC()

        elif entryname == "NTIMESTEPS":
            self.timeSteps.setText(entryvalue)
            self.gpFlag[10] = 1
            return

        elif entryname == "NSMOOTH":
            self.Nsmooth.setText(entryvalue)
            self.gpFlag[11] = 1
            return

        elif entryname == "SAVET":
            self.saveAt.setText(entryvalue)
            self.gpFlag[12] = 1
            return
        
        elif entryname == "RESTART":
            self.reStart.setValue(int(entryvalue))
            return
        
        elif entryname == "STARTTIME":
            self.startTime.setText(entryvalue)
            return

        elif entryname == "numworkers":
            self.numWorkers.setText(entryvalue)
            return

        elif entryname == "COMPONENTS":
            entryvalue = entryvalue.replace("{","")
            entryvalue = entryvalue.replace("}","")
            entryvalue = entryvalue.replace(",","\n")
            self.ctext.setPlainText(entryvalue)
            self.componentSaveBtnClicked()
            self.gpFlag[13] = 1
            return

        elif entryname == "PHASES":
            entryvalue = entryvalue.replace("{","")
            entryvalue = entryvalue.replace("}","")
            entryvalue = entryvalue.replace(",","\n")
            self.ptext.setPlainText(entryvalue)
            self.phaseSaveBtnClicked()
            self.gpFlag[14] = 1
            return

        elif entryname == "GAMMA":
            entryvalue = entryvalue.replace("{","")
            entryvalue = entryvalue.replace("}","")
            self.gammaInput.setText(entryvalue)
            self.gpFlag[15] = 1
            return

        elif entryname == "DIFFUSIVITY":
            
            self.NextBtn3()
            self.gpFlag[16] = self.gpFlag[16] + 1
            entryvalue = entryvalue.replace("{","")
            entryvalue = entryvalue.replace("}","")

            Diffdata = entryvalue.split(",")

            self.DiffusivityType[int(Diffdata[1])] = Diffdata[0]
            self.Diffusivity[int(Diffdata[1])] = ",".join(Diffdata[2:])


        elif entryname == "R":
            self.R_Value.setText(entryvalue)
            self.gpFlag[17] = 1

        elif entryname == "V":
            self.V_Value.setText(entryvalue)
            self.gpFlag[18] = 1

        elif entryname == "EIGEN_STRAIN":
            entryvalue = entryvalue.replace("{","")
            entryvalue = entryvalue.replace("}","")
            ESdata = entryvalue.split(",")
            self.eigenStrain[int(ESdata[0])] = ",".join(ESdata[1:])
            self.gpFlag[19] = self.gpFlag[19] +1


        elif entryname == "VOIGT_ISOTROPIC":
            entryvalue = entryvalue.replace("{","")
            entryvalue = entryvalue.replace("}","")
            ECdata = entryvalue.split(",")
            self.gpFlag[20] = self.gpFlag[20] +1

            self.elasticType[int(ECdata[0])] = "0"
            self.elasticConstant[int(ECdata[0])] = ",".join(ECdata[1:])


        elif entryname == "VOIGT_CUBIC":
            entryvalue = entryvalue.replace("{","")
            entryvalue = entryvalue.replace("}","")
            ECdata = entryvalue.split(",")
            self.elasticType[int(ECdata[0])] = "1"
            self.elasticConstant[int(ECdata[0])] = ",".join(ECdata[1:])
            self.gpFlag[20] = self.gpFlag[20] +1

        elif entryname == "VOIGT_TETRAGONAL":
            entryvalue = entryvalue.replace("{","")
            entryvalue = entryvalue.replace("}","")
            ECdata = entryvalue.split(",")
            self.elasticType[int(ECdata[0])] = "2"
            self.elasticConstant[int(ECdata[0])] = ",".join(ECdata[1:])
            self.gpFlag[20] = self.gpFlag[20] +1


        elif entryname == "BOUNDARY":
            entryvalue = entryvalue.replace("{","")
            entryvalue = entryvalue.replace("}","")
            BC_Cond = entryvalue.split(",")

            if BC_Cond[0] == "phi":
                self.pDropdown_2.setCurrentIndex(1)
                self.Bcnd[0] = ",".join(BC_Cond[1:5])
                self.gpFlag[21] = 1

            elif BC_Cond[0] == "mu":
                self.pDropdown_2.setCurrentIndex(2)
                self.Bcnd[1] = ",".join(BC_Cond[1:5])
                self.gpFlag[22] = 1

            elif BC_Cond[0] == "c":
                self.Bcnd[2] = ",".join(BC_Cond[1:5])
                self.gpFlag[22] = 1

            elif BC_Cond[0] == "T":
                self.Bcnd[3] = ",".join(BC_Cond[1:5])
                self.gpFlag[23] = 1

        elif entryname == "BOUNDARY_VALUE":
            entryvalue = entryvalue.replace("{","")
            entryvalue = entryvalue.replace("}","")
            BC_Cond = entryvalue.split(",")

            if BC_Cond[0] == "phi":
                self.BconV[0] = ",".join(BC_Cond[1:5])
                self.gpFlag[24] = 1

            elif BC_Cond[0] == "mu":
                self.BconV[1] = ",".join(BC_Cond[1:5])
                self.gpFlag[25] = 1

            elif BC_Cond[0] == "c":
                self.BconV[2] = ",".join(BC_Cond[1:5])
                self.gpFlag[25] = 1

            elif BC_Cond[0] == "T":
                self.BconV[3] = ",".join(BC_Cond[1:5])
                self.gpFlag[26] = 1


        self.pDropdown_2.setCurrentIndex(0)
        if self.DiffusivityType[0] == 1:
            self.diffR_2.setChecked(True)
        elif self.DiffusivityType[0] == 0:
            self.diffR.setChecked(True)

        self.diffInput.setText(self.Diffusivity[0])
        self.Estrain.setText( self.eigenStrain[0])
        self.Econstant.setText(self.elasticConstant[0])
        self.clickedBtn1()
        self.radio_GP.setChecked(True)

        ## Material Specific Parameter

        if entryname == "ISOTHERMAL":
            if entryvalue == "1":
                self.thermalYGP.setChecked(True)
                self.thermalNGP.setChecked(False)

            elif entryvalue == "0":
                self.thermalYGP.setChecked(False)
                self.thermalNGP.setChecked(True)


        elif entryname == "BINARY" and entryvalue == "1":
            self.simTypeGP.setCurrentIndex(0)

        elif entryname == "TERNARY" and entryvalue == "1":
            self.simTypeGP.setCurrentIndex(1)

        elif entryname == "DILUTE" and entryvalue == "1":
            self.simTypeGP.setCurrentIndex(2)

        elif entryname == "T":
            self.TGP.setText(entryvalue)

        elif entryname == "WRITEFORMAT":
            if entryvalue =="ASCII":
                self.writeFormatGP.setCurrentIndex(0)
            elif entryvalue =="BINARY":
                self.writeFormatGP.setCurrentIndex(1)

        elif entryname == "WRITEHDF5":
            self.writehdfGP.setValue(int(entryvalue))

        elif entryname == "TRACK_PROGRESS":
            self.trackProgressGP.setText(entryvalue)

        elif entryname == "epsilon":
            self.epsilonGP.setText(entryvalue)

        elif entryname == "tau":
            self.tauGP.setText(entryvalue)

        elif entryname == "Tau":
            entryvalue = entryvalue.replace("{","")
            entryvalue = entryvalue.replace("}","")
            self.TauGP.setText(entryvalue)

        elif entryname == "Function_anisotropy":
            self.FanisotropyGP.setText(entryvalue)

        elif entryname == "Anisotropy_type":
            self.anisotropyTypeGP.setText(entryvalue)

        elif entryname == "dab":
            entryvalue = entryvalue.replace("{","")
            entryvalue = entryvalue.replace("}","")
            self.debGP.setText(entryvalue)

        elif entryname == "Function_W":
            self.funcWGP.setText(entryvalue)

        elif entryname == "Gamma_abc":
            entryvalue = entryvalue.replace("{","")
            entryvalue = entryvalue.replace("}","")
            self.gammaABCGP.setText(entryvalue)

        elif entryname == "Shift":
            self.shiftGP.setValue(int(entryvalue))

        elif entryname == "Shiftj":
            self.shiftJGP.setText(entryvalue)

        elif entryname == "Writecomposition":
            self.writecompGP.setText(entryvalue)


        elif entryname == "Noise_phasefield":
            self.noiseGP.setValue(int(entryvalue))

        elif entryname == "Amp_Noise_Phase":
            self.ampNoiseGP.setText(entryvalue)


        elif entryname == "Equilibrium_temperature":
            self.equTGP.setText(entryvalue)

        elif entryname == "Filling_temperature":
            self.fillingTGP.setText(entryvalue)

        elif entryname == "Tempgrady":
            entryvalue = entryvalue.replace("{","")
            entryvalue = entryvalue.replace("}","")
            self.tempgradyGP.setText(entryvalue)

        elif entryname == "Function_F":
            self.funcFGP.setText(entryvalue)

        elif entryname == "A":
            entryvalue = entryvalue.replace("{","")
            entryvalue = entryvalue.replace("}","")
            Avalue = entryvalue.split(",")
            self.tableWidgetGPA.setItem(int(Avalue[0]),1, QTableWidgetItem(str(", ".join(Avalue[1:]))))

        elif entryname == "ceq":
            entryvalue = entryvalue.replace("{","")
            entryvalue = entryvalue.replace("}","")
            ceqvalue = entryvalue.split(",")
            k=self.noP.value()

            for i in range(k*k):
                if self.tableWidgetGP.item(i,0).text() == ceqvalue[0] and self.tableWidgetGP.item(i,1).text() == ceqvalue[1]:
                    self.tableWidgetGP.setItem(i,2, QTableWidgetItem(str( ", ".join(ceqvalue[2:]))))

        elif entryname == "cfill":
            entryvalue = entryvalue.replace("{","")
            entryvalue = entryvalue.replace("}","")
            ceqvalue = entryvalue.split(",")
            k=self.noP.value()

            for i in range(k*k):
                if self.tableWidgetGP.item(i,0).text() == ceqvalue[0] and self.tableWidgetGP.item(i,1).text() == ceqvalue[1]:
                    self.tableWidgetGP.setItem(i,3, QTableWidgetItem(str( ", ".join(ceqvalue[2:]))))

        elif entryname == "slopes":
            entryvalue = entryvalue.replace("{","")
            entryvalue = entryvalue.replace("}","")
            ceqvalue = entryvalue.split(",")
            k=self.noP.value()

            for i in range(k*k):
                if self.tableWidgetGP.item(i,0).text() == ceqvalue[0] and self.tableWidgetGP.item(i,1).text() == ceqvalue[1]:
                    self.tableWidgetGP.setItem(i,4, QTableWidgetItem(str( ", ".join(ceqvalue[2:]))))

        elif entryname == "Rotation_matrix":
            entryvalue = entryvalue.replace("{","")
            entryvalue = entryvalue.replace("}","")
            ceqvalue = entryvalue.split(",")
            k=self.noP.value()

            for i in range(k*k):
                if self.tableWidgetGP.item(i,0).text() == ceqvalue[0] and self.tableWidgetGP.item(i,1).text() == ceqvalue[1]:
                    self.tableWidgetGP.setItem(i,5, QTableWidgetItem(str( ", ".join(ceqvalue[2:]))))


    def fillGPCheck(self):
        self.errorListGP = []
        noP_value = self.noP.value()

        for i in range(noP_value):
            if self.tableWidgetGPA.item(i,1) is None or self.tableWidgetGPA.item(i,1).text() == '':
                self.errorListGP.append("A value for phase " + str(i))

        for i in range(noP_value*noP_value):
            for j in range(2,6,1):
                if self.tableWidgetGP.item(i,j) is None or self.tableWidgetGP.item(i,j).text() == '':
                    self.errorListGP.append("ceq or cfill or slopes ")


        if self.trackProgressGP.text() == "":
            self.errorListGP.append("Track Progress  ")

        if self.epsilonGP.text() == "":
            self.errorListGP.append("Epsilon ")

        if self.tauGP.text() == "":
            self.errorListGP.append("tau ")

        if self.TauGP.text() == "":
            self.errorListGP.append("Tau")

        if len(self.TauGP.text().split(",")) != (noP_value * ((noP_value - 1) / 2)):
            self.errorListGP.append("Invalid tuple length of Tau")

        if self.FanisotropyGP.text() == "":
            self.errorListGP.append("Function Anisotropy")

        if self.anisotropyTypeGP.text() == "":
            self.errorListGP.append("Anisotropy Type")

        if self.debGP.text() == "":
            self.errorListGP.append("dab")
            return False

        if len(self.debGP.text().split(",")) != int(noP_value * ((noP_value - 1) / 2)):
            self.errorListGP.append("Invalid tuple length of dab")

        if self.funcWGP.text() == "":
            self.errorListGP.append("Function W")

        if self.funcFGP.text() =="":
            self.errorListGP.append("Function F")


        if len(self.gammaABCGP.text().split(",")) != int(noP_value * ((noP_value - 1)*(noP_value - 2) / 6)) and self.gammaABCGP.text() != "":
            self.errorListGP.append("Invalid length of Gamma_abc")

        if self.shiftGP.value() > 1:
            self.errorListGP.append("Shift")

        if self.shiftJGP.text() =="":
            self.errorListGP.append("Shift J")

        if self.equTGP.text() == "":
            self.errorListGP.append("Equilibrium Temperature")

        if self.fillingTGP.text() =="":
            self.errorListGP.append("Filling Temperature")

        if self.TGP.text() =="":
            self.errorListGP.append("Temperature")

        if self.tempgradyGP.text() == "":
            self.errorListGP.append("Tempgrady")

        if len(self.tempgradyGP.text().split(",")) != 5:
            self.errorListGP.append("Invalid tuple length of Tempgrady")

        if self.ampNoiseGP.text() =="" and self.noiseGP.value() == 1:
            self.errorListGP.append("Amp_Noise_Phase")

        if self.writecompGP.text() == "":
            self.errorListGP.append("Writecomposition")


    def fillEntryCH(self,entryname, entryvalue):
        #print(entryvalue)

        if entryname == "DIMENSION":
            self.dim.setValue(int(entryvalue))
            self.chFlag[0] = 1
            return

        elif entryname == "MESH_X":
            self.mesh_x.setText(entryvalue)
            self.chFlag[1] = 1
            return

        elif entryname == "MESH_Y":
            self.mesh_y.setText(entryvalue)
            self.chFlag[2] = 1
            return

        elif entryname == "MESH_Z":
            self.mesh_z.setText(entryvalue)
            self.chFlag[3] = 1
            return

        elif entryname == "DELTA_X":
            self.dx.setText(entryvalue)
            self.chFlag[4] = 1
            return

        elif entryname == "DELTA_Y":
            self.dy.setText(entryvalue)
            self.chFlag[5] = 1
            return

        elif entryname == "DELTA_Z":
            self.dz.setText(entryvalue)
            self.chFlag[6] = 1
            return

        elif entryname == "DELTA_t":
            self.dt.setText(entryvalue)
            self.chFlag[7] = 1
            return

        elif entryname == "NUMPHASES":
            self.noP.setValue(int(entryvalue))
            self.chFlag[8] = 1
            #self.updateNoP()
            return

        elif entryname == "NUMCOMPONENTS":
            self.noC.setValue(int(entryvalue))
            self.chFlag[9] = 1
            #self.updateNoC()
            return

        elif entryname == "NTIMESTEPS":
            self.timeSteps.setText(entryvalue)
            self.chFlag[10] = 1
            return

        elif entryname == "NSMOOTH":
            self.Nsmooth.setText(entryvalue)
            self.chFlag[11] = 1
            return

        elif entryname == "SAVET":
            self.saveAt.setText(entryvalue)
            self.chFlag[12] = 1
            return

        elif entryname == "RESTART":
            self.reStart.setValue(int(entryvalue))
            return
        
        elif entryname == "STARTTIME":
            self.startTime.setText(entryvalue)
            return

        elif entryname == "numworkers":
            self.numWorkers.setText(entryvalue)
            return


        elif entryname == "COMPONENTS":
            entryvalue = entryvalue.replace("{","")
            entryvalue = entryvalue.replace("}","")
            entryvalue = entryvalue.replace(",","\n")
            self.ctext.setPlainText(entryvalue)
            self.chFlag[13] = 1
            return

        elif entryname == "PHASES":
            entryvalue = entryvalue.replace("{","")
            entryvalue = entryvalue.replace("}","")
            entryvalue = entryvalue.replace(",","\n")
            self.ptext.setPlainText(entryvalue)
            self.chFlag[14] = 1
            return

        elif entryname == "R":
            self.R_Value.setText(entryvalue)
            self.chFlag[15] = 1
            return

        elif entryname == "V":
            self.V_Value.setText(entryvalue)
            self.chFlag[16] = 1
            return

        self.NextBtn3()

        for i in range(self.noP.value()):
            self.DiffusivityType[i] = "1"
            self.Diffusivity[i] =  "1"+ ",1"*(self.noP.value()-2)
            self.eigenStrain[i] = "0.01, 0.01, 0.0, 0.0, 0.0, 0.0"
            self.elasticType[i] = "0"
            self.elasticConstant[i] = "270, 187.5, 125.0"
        

        self.diffInput.setText("1")
        self.Estrain.setText( "0.01, 0.01, 0.0, 0.0, 0.0, 0.0")
        self.Econstant.setText("270, 187.5, 125.0")

        self.gammaInput.setText("1.0")
        self.clickedBtn1()
        self.radio_CH.setChecked(True)

        ## Material Specific Parameter
        for i in range(4):
            self.Bcnd[i] = "1,1,1,1"
            self.BconV[i] = "1,1,1,1"


        if entryname == "WRITEFORMAT":
            self.chFlag[17] = 1
            if entryvalue =="ASCII":
                self.writeFormatCH.setCurrentIndex(0)
            elif entryvalue =="BINARY":
                self.writeFormatCH.setCurrentIndex(1)

        elif entryname == "TRACK_PROGRESS":
            self.trackProgressCH.setText(entryvalue)
            self.chFlag[18] = 1

        elif entryname == "L_phi":
            entryvalue = entryvalue.replace("{","")
            entryvalue = entryvalue.replace("}","")
            self.lPhiCH.setText(entryvalue)
            self.chFlag[19] = 1

        elif entryname == "Kappa_phi":
            entryvalue = entryvalue.replace("{","")
            entryvalue = entryvalue.replace("}","")
            self.kappaPhiCH.setText(entryvalue)
            self.chFlag[20] = 1

        elif entryname == "Kappa_c":
            entryvalue = entryvalue.replace("{","")
            entryvalue = entryvalue.replace("}","")
            self.kappaCCH.setText(entryvalue)
            self.chFlag[21] = 1

        elif entryname == "A_fm":
            entryvalue = entryvalue.replace("{","")
            entryvalue = entryvalue.replace("}","")
            self.afmCH.setText(entryvalue)
            self.chFlag[22] = 1

        elif entryname == "B_fp":
            entryvalue = entryvalue.replace("{","")
            entryvalue = entryvalue.replace("}","")
            self.bfpCH.setText(entryvalue)
            self.chFlag[23] = 1

        elif entryname == "spinodal":
            self.spinodalCH.setValue(int(entryvalue))

        elif entryname == "tdbflag":
            self.tdbflagCH.setValue(int(entryvalue))

        elif entryname == "tdbfname":
            self.tdbfnameCH.setText(entryvalue)

        elif entryname == "AtomicMobility":
            self.chFlag[24] =self.chFlag[24] + 1
            entryvalue = entryvalue.replace("{","")
            entryvalue = entryvalue.replace("}","")
            entryvalue = entryvalue.replace("\n","")
            AMvalue = entryvalue.split(",")
            if int(AMvalue[0]) == 1:
                self.tableWidgetCHA.setItem(int(AMvalue[1]),1, QTableWidgetItem(str("DM")))
            else:
                self.tableWidgetCHA.setItem(int(AMvalue[1]),1, QTableWidgetItem(str("FM")))
            self.tableWidgetCHA.setItem(int(AMvalue[1]),2, QTableWidgetItem(str(", ".join(AMvalue[2:]))))

        elif entryname == "ceq":
            self.chFlag[25] =self.chFlag[25] + 1
            entryvalue = entryvalue.replace("{","")
            entryvalue = entryvalue.replace("}","")
            ceqvalue = entryvalue.split(",")
            k=self.noP.value()

            for i in range(k*k):
                if self.tableWidgetCH.item(i,0).text() == ceqvalue[0] and self.tableWidgetCH.item(i,1).text() == ceqvalue[1]:
                    self.tableWidgetCH.setItem(i,2, QTableWidgetItem(str( ", ".join(ceqvalue[2:]))))

        elif entryname == "cfill":
            self.chFlag[25] =self.chFlag[25] + 1
            entryvalue = entryvalue.replace("{","")
            entryvalue = entryvalue.replace("}","")
            ceqvalue = entryvalue.split(",")
            k=self.noP.value()

            for i in range(k*k):
                if self.tableWidgetCH.item(i,0).text() == ceqvalue[0] and self.tableWidgetCH.item(i,1).text() == ceqvalue[1]:
                    self.tableWidgetCH.setItem(i,3, QTableWidgetItem(str( ", ".join(ceqvalue[2:]))))


    def fillEntryKKS(self,entryname, entryvalue):
        #print(entryvalue)

        if entryname == "DIMENSION":
            self.dim.setValue(int(entryvalue))
            self.kksFlag[0] = 1
            return

        elif entryname == "MESH_X":
            self.mesh_x.setText(entryvalue)
            self.kksFlag[1] = 1
            return

        elif entryname == "MESH_Y":
            self.mesh_y.setText(entryvalue)
            self.kksFlag[2] = 1
            return

        elif entryname == "MESH_Z":
            self.mesh_z.setText(entryvalue)
            self.kksFlag[3] = 1
            return

        elif entryname == "DELTA_X":
            self.dx.setText(entryvalue)
            self.kksFlag[4] = 1
            return

        elif entryname == "DELTA_Y":
            self.dy.setText(entryvalue)
            self.kksFlag[5] = 1
            return

        elif entryname == "DELTA_Z":
            self.dz.setText(entryvalue)
            self.kksFlag[6] = 1
            return

        elif entryname == "DELTA_t":
            self.dt.setText(entryvalue)
            self.kksFlag[7] = 1
            return

        elif entryname == "NUMPHASES":
            self.noP.setValue(int(entryvalue))
            self.kksFlag[8] = 1
            return
            #self.updateNoP()

        elif entryname == "NUMCOMPONENTS":
            self.noC.setValue(int(entryvalue))
            self.kksFlag[9] = 1
            return
            #self.updateNoC()

        elif entryname == "NTIMESTEPS":
            self.timeSteps.setText(entryvalue)
            self.kksFlag[10] = 1
            return

        elif entryname == "NSMOOTH":
            self.Nsmooth.setText(entryvalue)
            self.kksFlag[11] = 1
            return

        elif entryname == "SAVET":
            self.saveAt.setText(entryvalue)
            self.kksFlag[12] = 1
            return

        elif entryname == "RESTART":
            self.reStart.setValue(int(entryvalue))
            return
        
        elif entryname == "STARTTIME":
            self.startTime.setText(entryvalue)
            return

        elif entryname == "numworkers":
            self.numWorkers.setText(entryvalue)
            return


        elif entryname == "COMPONENTS":
            entryvalue = entryvalue.replace("{","")
            entryvalue = entryvalue.replace("}","")
            entryvalue = entryvalue.replace(",","\n")
            self.ctext.setPlainText(entryvalue)
            self.kksFlag[13] = 1
            return

        elif entryname == "PHASES":
            entryvalue = entryvalue.replace("{","")
            entryvalue = entryvalue.replace("}","")
            entryvalue = entryvalue.replace(",","\n")
            self.ptext.setPlainText(entryvalue)
            self.kksFlag[14] = 1
            return

        elif entryname == "GAMMA":
            entryvalue = entryvalue.replace("{","")
            entryvalue = entryvalue.replace("}","")
            self.gammaInput.setText(entryvalue)
            self.kksFlag[15] = 1
            return

        elif entryname == "DIFFUSIVITY":
            self.NextBtn3()
            self.kksFlag[16] = self.kksFlag[16] +  1
            entryvalue = entryvalue.replace("{","")
            entryvalue = entryvalue.replace("}","")

            Diffdata = entryvalue.split(",")

            self.DiffusivityType[int(Diffdata[1])] = Diffdata[0]
            self.Diffusivity[int(Diffdata[1])] = ",".join(Diffdata[2:])

        elif entryname == "R":
            self.R_Value.setText(entryvalue)
            self.kksFlag[17] = 1

        elif entryname == "V":
            self.V_Value.setText(entryvalue)
            self.kksFlag[18] = 1

        elif entryname == "EIGEN_STRAIN":
            entryvalue = entryvalue.replace("{","")
            entryvalue = entryvalue.replace("}","")
            ESdata = entryvalue.split(",")
            self.eigenStrain[int(ESdata[0])] = ",".join(ESdata[1:])
            self.kksFlag[19] = self.kksFlag[19] + 1


        elif entryname == "VOIGT_ISOTROPIC":
            entryvalue = entryvalue.replace("{","")
            entryvalue = entryvalue.replace("}","")
            ECdata = entryvalue.split(",")

            self.elasticType[int(ECdata[0])] = "0"
            self.elasticConstant[int(ECdata[0])] = ",".join(ECdata[1:])
            self.kksFlag[20] = self.kksFlag[20] + 1


        elif entryname == "VOIGT_CUBIC":
            entryvalue = entryvalue.replace("{","")
            entryvalue = entryvalue.replace("}","")
            ECdata = entryvalue.split(",")
            self.elasticType[int(ECdata[0])] = "1"
            self.elasticConstant[int(ECdata[0])] = ",".join(ECdata[1:])
            self.kksFlag[20] = self.kksFlag[20] + 1


        elif entryname == "VOIGT_TETRAGONAL":
            entryvalue = entryvalue.replace("{","")
            entryvalue = entryvalue.replace("}","")
            ECdata = entryvalue.split(",")
            self.elasticType[int(ECdata[0])] = "2"
            self.elasticConstant[int(ECdata[0])] = ",".join(ECdata[1:])
            self.kksFlag[20] = self.kksFlag[20] + 1


        elif entryname == "BOUNDARY":
            entryvalue = entryvalue.replace("{","")
            entryvalue = entryvalue.replace("}","")
            BC_Cond = entryvalue.split(",")

            if BC_Cond[0] == "phi":
                self.pDropdown_2.setCurrentIndex(1)
                self.Bcnd[0] = ",".join(BC_Cond[1:5])
                self.kksFlag[21] =  + 1

            elif BC_Cond[0] == "mu":
                self.pDropdown_2.setCurrentIndex(2)
                self.Bcnd[1] = ",".join(BC_Cond[1:5])
                self.kksFlag[22] = 1

            elif BC_Cond[0] == "c":
                self.Bcnd[2] = ",".join(BC_Cond[1:5])
                self.kksFlag[22] =  self.kksFlag[22] + 1

            elif BC_Cond[0] == "T":
                self.Bcnd[3] = ",".join(BC_Cond[1:5])
                self.kksFlag[23] = 1

        elif entryname == "BOUNDARY_VALUE":
            entryvalue = entryvalue.replace("{","")
            entryvalue = entryvalue.replace("}","")
            BC_Cond = entryvalue.split(",")

            if BC_Cond[0] == "phi":
                self.BconV[0] = ",".join(BC_Cond[1:5])
                self.kksFlag[24] =  1

            elif BC_Cond[0] == "mu":
                self.BconV[1] = ",".join(BC_Cond[1:5])
                self.kksFlag[25] =  1

            elif BC_Cond[0] == "c":
                self.BconV[2] = ",".join(BC_Cond[1:5])
                self.kksFlag[25] = self.kksFlag[25] + 1

            elif BC_Cond[0] == "T":
                self.BconV[3] = ",".join(BC_Cond[1:5])
                self.kksFlag[26] =  1


        self.pDropdown_2.setCurrentIndex(0)
        if self.DiffusivityType[0] == 1:
            self.diffR_2.setChecked(True)
        elif self.DiffusivityType[0] == 0:
            self.diffR.setChecked(True)

        self.diffInput.setText(self.Diffusivity[0])
        self.Estrain.setText( self.eigenStrain[0])
        self.Econstant.setText(self.elasticConstant[0])
        self.clickedBtn1()
        self.radio_KKR.setChecked(True)

        ## Material Specific Parameter

        if entryname == "WRITEFORMAT":
            self.kksFlag[27] = 1
            if entryvalue =="ASCII":
                self.writeFormatKKS.setCurrentIndex(0)
            elif entryvalue =="BINARY":
                self.writeFormatKKS.setCurrentIndex(1)

        elif entryname == "TRACK_PROGRESS":
            self.trackprogressKKS.setText(entryvalue)
            self.kksFlag[28] = 1

        elif entryname == "ELAST_INT":
            self.elastIntKKS.setText(entryvalue)
            self.kksFlag[29] = 1

        elif entryname == "relax_coeff":
            self.relaxCoeffKKS.setText(entryvalue)
            self.kksFlag[30] = 1

        elif entryname == "c0":
            self.CKKS.setText(entryvalue)
            self.kksFlag[31] = 1

        elif entryname == "alpha":
            self.alphaKKS.setText(entryvalue)
            self.kksFlag[32] = 1


        elif entryname == "lambda":
            self.lambdaKKS.setText(entryvalue)
            self.kksFlag[33] = 1

        elif entryname == "tdbfname":
            self.tdbfnameKKS.setText(entryvalue)

        elif entryname == "f0":
            entryvalue = entryvalue.replace("{","")
            entryvalue = entryvalue.replace("}","")
            f0value = entryvalue.split(",")
            self.tableWidgetKKSF.setItem(int(f0value[0]),1, QTableWidgetItem(str(f0value[1])))
            self.kksFlag[34] = self.kksFlag[34] + 1

        elif entryname == "Noise_phasefield":
            self.noiseKKS.setValue(int(entryvalue))
            self.kksFlag[35] = 1

        elif entryname == "Amp_Noise_Phase":
            self.ampNoiseKKS.setText(entryvalue)
            self.kksFlag[36] = 1

        elif entryname == "ceq":
            entryvalue = entryvalue.replace("{","")
            entryvalue = entryvalue.replace("}","")
            ceqvalue = entryvalue.split(",")
            self.kksFlag[37] = self.kksFlag[37] + 1
            k=self.noP.value()

            for i in range(k*k):
                if self.tableWidgetKKS.item(i,0).text() == ceqvalue[0] and self.tableWidgetKKS.item(i,1).text() == ceqvalue[1]:
                    self.tableWidgetKKS.setItem(i,2, QTableWidgetItem(str( ", ".join(ceqvalue[2:]))))


    def fillEntryKKS2(self,entryname, entryvalue):
        #print(entryvalue)
        self.kks2Flag[32] =  1

        if entryname == "DIMENSION":
            self.dim.setValue(int(entryvalue))
            self.kks2Flag[0] = 1
            return

        elif entryname == "MESH_X":
            self.mesh_x.setText(entryvalue)
            self.kks2Flag[1] = 1
            return

        elif entryname == "MESH_Y":
            self.mesh_y.setText(entryvalue)
            self.kks2Flag[2] = 1
            return

        elif entryname == "MESH_Z":
            self.mesh_z.setText(entryvalue)
            self.kks2Flag[3] = 1
            return

        elif entryname == "DELTA_X":
            self.dx.setText(entryvalue)
            self.kks2Flag[4] = 1
            return

        elif entryname == "DELTA_Y":
            self.dy.setText(entryvalue)
            self.kks2Flag[5] = 1
            return

        elif entryname == "DELTA_Z":
            self.dz.setText(entryvalue)
            self.kks2Flag[6] = 1
            return

        elif entryname == "DELTA_t":
            self.dt.setText(entryvalue)
            self.kks2Flag[7] = 1
            return

        elif entryname == "NUMPHASES":
            self.noP.setValue(int(entryvalue))
            self.kks2Flag[8] = 1
            return
            #self.updateNoP()

        elif entryname == "NUMCOMPONENTS":
            self.noC.setValue(int(entryvalue))
            self.kks2Flag[9] = 1
            return
            #self.updateNoC()

        elif entryname == "NTIMESTEPS":
            self.timeSteps.setText(entryvalue)
            self.kks2Flag[10] = 1
            return

        elif entryname == "NSMOOTH":
            self.Nsmooth.setText(entryvalue)
            self.kks2Flag[11] = 1
            return

        elif entryname == "SAVET":
            self.saveAt.setText(entryvalue)
            self.kks2Flag[12] = 1
            return

        elif entryname == "RESTART":
            self.reStart.setValue(int(entryvalue))
            return
        
        elif entryname == "STARTTIME":
            self.startTime.setText(entryvalue)
            return

        elif entryname == "numworkers":
            self.numWorkers.setText(entryvalue)
            return


        elif entryname == "COMPONENTS":
            entryvalue = entryvalue.replace("{","")
            entryvalue = entryvalue.replace("}","")
            entryvalue = entryvalue.replace(",","\n")
            self.ctext.setPlainText(entryvalue)
            self.kks2Flag[13] = 1
            return

        elif entryname == "PHASES":
            entryvalue = entryvalue.replace("{","")
            entryvalue = entryvalue.replace("}","")
            entryvalue = entryvalue.replace(",","\n")
            self.ptext.setPlainText(entryvalue)
            self.kks2Flag[14] = 1
            return

        elif entryname == "GAMMA":
            entryvalue = entryvalue.replace("{","")
            entryvalue = entryvalue.replace("}","")
            self.gammaInput.setText(entryvalue)
            self.kks2Flag[15] = 1
            return

        elif entryname == "DIFFUSIVITY":
            self.NextBtn3()

            entryvalue = entryvalue.replace("{","")
            entryvalue = entryvalue.replace("}","")

            Diffdata = entryvalue.split(",")

            self.DiffusivityType[int(Diffdata[1])] = Diffdata[0]
            self.Diffusivity[int(Diffdata[1])] = ",".join(Diffdata[2:])
            self.kks2Flag[16] = self.kks2Flag[16] + 1

        elif entryname == "R":
            self.R_Value.setText(entryvalue)
            self.kks2Flag[17] = 1

        elif entryname == "V":
            self.V_Value.setText(entryvalue)
            self.kks2Flag[18] = 1


        elif entryname == "BOUNDARY":
            entryvalue = entryvalue.replace("{","")
            entryvalue = entryvalue.replace("}","")
            BC_Cond = entryvalue.split(",")

            if BC_Cond[0] == "phi":
                self.pDropdown_2.setCurrentIndex(1)
                self.Bcnd[0] = ",".join(BC_Cond[1:5])
                self.kks2Flag[19] =  1

            elif BC_Cond[0] == "mu":
                self.pDropdown_2.setCurrentIndex(2)
                self.Bcnd[1] = ",".join(BC_Cond[1:5])
                self.kks2Flag[20] =  1

            elif BC_Cond[0] == "c":
                self.Bcnd[2] = ",".join(BC_Cond[1:5])
                self.kks2Flag[20] =  1

            elif BC_Cond[0] == "T":
                self.Bcnd[3] = ",".join(BC_Cond[1:5])
                self.kks2Flag[21] =  1

        elif entryname == "BOUNDARY_VALUE":
            entryvalue = entryvalue.replace("{","")
            entryvalue = entryvalue.replace("}","")
            BC_Cond = entryvalue.split(",")

            if BC_Cond[0] == "phi":
                self.BconV[0] = ",".join(BC_Cond[1:5])
                self.kks2Flag[22] =  1

            elif BC_Cond[0] == "mu":
                self.BconV[1] = ",".join(BC_Cond[1:5])
                self.kks2Flag[23] =  1

            elif BC_Cond[0] == "c":
                self.BconV[2] = ",".join(BC_Cond[1:5])
                self.kks2Flag[23] =  1

            elif BC_Cond[0] == "T":
                self.BconV[3] = ",".join(BC_Cond[1:5])
                self.kks2Flag[24] =  1


        self.pDropdown_2.setCurrentIndex(0)
        if self.DiffusivityType[0] == 1:
            self.diffR_2.setChecked(True)
        elif self.DiffusivityType[0] == 0:
            self.diffR.setChecked(True)

        self.diffInput.setText(self.Diffusivity[0])

        for i in range(self.noP.value()):
            self.eigenStrain[i] = "0.01, 0.01, 0.0, 0.0, 0.0, 0.0"
            self.elasticType[i] = "0"
            self.elasticConstant[i] = "270, 187.5, 125.0"
        self.Estrain.setText( "0.01, 0.01, 0.0, 0.0, 0.0, 0.0")
        self.Econstant.setText("270, 187.5, 125.0")

        self.clickedBtn1()
        self.radio_KKS2.setChecked(True)

        ## Material Specific Parameter

        if entryname == "ISOTHERMAL":
            self.kks2Flag[25] =  1
            if entryvalue == 1:
                self.thermalYKKS2.setChecked(True)
                self.thermalNKKS2.setChecked(False)
            else:
                self.thermalNKKS2.setChecked(True)
                self.thermalYKKS2.setChecked(False)

        elif entryname == "BINARY" and entryvalue == "1":
            self.simTypeKKS2.setCurrentIndex(0)
            self.kks2Flag[26] =  1

        elif entryname == "TERNARY" and entryvalue == "1":
            self.simTypeKKS2.setCurrentIndex(1)
            self.kks2Flag[26] =  1

        elif entryname == "DILUTE" and entryvalue == "1":
            self.simTypeKKS2.setCurrentIndex(2)
            self.kks2Flag[26] =  1

        elif entryname == "WRITEFORMAT":
            self.kks2Flag[27] =  1
            if entryvalue =="ASCII":
                self.writeFormatKKS2.setCurrentIndex(0)

            elif entryvalue =="BINARY":
                self.writeFormatKKS2.setCurrentIndex(1)

        elif entryname == "TRACK_PROGRESS":
            self.trackProgressKKS2.setText(entryvalue)
            self.kks2Flag[28] =  1

        elif entryname == "epsilon":
            self.epsilonKKS2.setText(entryvalue)
            self.kks2Flag[29] =  1

        elif entryname == "Function_anisotropy":
            self.FanisotropyKKS2.setText(entryvalue)
            self.kks2Flag[30] =  1

        elif entryname == "dab":
            entryvalue = entryvalue.replace("{","")
            entryvalue = entryvalue.replace("}","")
            self.debKKS2.setText(entryvalue)
            self.kks2Flag[31] =  1

        elif entryname == "temperature":
            self.temperatureKKS2.setText(entryvalue)
            self.kks2Flag[32] =  1

        elif entryname == "Noise_phasefield":
            self.noiseKKS2.setValue(int(entryvalue))
            self.kks2Flag[33] =  1

        elif entryname == "Amp_Noise_Phase":
            self.ampNoiseKKS2.setText(entryvalue)
            self.kks2Flag[34] =  1

        elif entryname == "Tempgrady":
            entryvalue = entryvalue.replace("{","")
            entryvalue = entryvalue.replace("}","")
            self.tempGradyKKS2.setText(entryvalue)
            self.kks2Flag[35] =  1

        elif entryname == "tNoiseStart":
            self.tNoiseStartKKS2.setText(entryvalue)
            self.kks2Flag[36] =  1

        elif entryname == "TLiquidus":
            self.TLKKS2.setText(entryvalue)
            self.kks2Flag[37] =  1

        elif entryname == "atr":
            self.atrKKS2.setText(entryvalue)
            self.kks2Flag[38] =  1

        elif entryname == "CLplatformID":
            self.CLPidKKS2.setText(entryvalue)
            self.kks2Flag[39] =  1

        elif entryname == "CLdeviceID":
            self.CLDidKKS2.setText(entryvalue)
            self.kks2Flag[40] =  1

        elif entryname == "tdbfname":
            self.tdbfnameKKS2.setText(entryvalue)
            self.kks2Flag[41] =  1

        elif entryname == "ceq":
            self.kks2Flag[42] =  self.kks2Flag[42] + 1
            entryvalue = entryvalue.replace("{","")
            entryvalue = entryvalue.replace("}","")
            ceqvalue = entryvalue.split(",")
            k=self.noP.value()

            for i in range(k*k):
                if self.tableWidgetKKS2.item(i,0).text() == ceqvalue[0] and self.tableWidgetKKS2.item(i,1).text() == ceqvalue[1]:
                    self.tableWidgetKKS2.setItem(i,2, QTableWidgetItem(str( ", ".join(ceqvalue[2:]))))
        elif entryname == "cfill":
            self.kks2Flag[43] =  self.kks2Flag[43] + 1
            entryvalue = entryvalue.replace("{","")
            entryvalue = entryvalue.replace("}","")
            ceqvalue = entryvalue.split(",")
            k=self.noP.value()

            for i in range(k*k):
                if self.tableWidgetKKS2.item(i,0).text() == ceqvalue[0] and self.tableWidgetKKS2.item(i,1).text() == ceqvalue[1]:
                    self.tableWidgetKKS2.setItem(i,3, QTableWidgetItem(str( ", ".join(ceqvalue[2:]))))


        elif entryname == "Rotation_matrix":
            self.kks2Flag[44] =  self.kks2Flag[44] + 1
            entryvalue = entryvalue.replace("{","")
            entryvalue = entryvalue.replace("}","")
            ceqvalue = entryvalue.split(",")
            k=self.noP.value()

            for i in range(k*k):
                if self.tableWidgetKKS2.item(i,0).text() == ceqvalue[0] and self.tableWidgetKKS2.item(i,1).text() == ceqvalue[1]:
                    self.tableWidgetKKS2.setItem(i,4, QTableWidgetItem(str( ", ".join(ceqvalue[2:]))))

#main

app = QApplication(sys.argv)
dir_ = QtCore.QDir("Ubuntu")
QtGui.QFontDatabase.addApplicationFont("resources/font/Ubuntu-Bold.ttf")
QtGui.QFontDatabase.addApplicationFont("resources/font/Ubuntu-Regular.ttf")
mainScreen = StartScreen()
widget = QtWidgets.QStackedWidget()
widget.addWidget(mainScreen)
widget.setFixedHeight(600)
widget.setFixedWidth(1000)
widget.setWindowTitle("MicroSim - Microstructure Simulator")
widget.setWindowIcon(QtGui.QIcon('resources/Mlogo.png'))
widget.show()

try:
    sys.exit(app.exec_())
except:
    print("Exiting")
