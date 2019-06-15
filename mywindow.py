# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mywindow.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MyWindow(object):
    def setupUi(self, MyWindow):
        MyWindow.setObjectName("MyWindow")
        MyWindow.resize(758, 550)
        self.groupBox = QtWidgets.QGroupBox(MyWindow)
        self.groupBox.setEnabled(False)
        self.groupBox.setGeometry(QtCore.QRect(30, 170, 681, 361))
        self.groupBox.setFlat(True)
        self.groupBox.setObjectName("groupBox")
        self.btn_infusion = QtWidgets.QPushButton(self.groupBox)
        self.btn_infusion.setGeometry(QtCore.QRect(50, 40, 75, 41))
        self.btn_infusion.setObjectName("btn_infusion")
        self.btn_channel1 = QtWidgets.QPushButton(self.groupBox)
        self.btn_channel1.setGeometry(QtCore.QRect(50, 150, 75, 41))
        self.btn_channel1.setObjectName("btn_channel1")
        self.btn_channel2 = QtWidgets.QPushButton(self.groupBox)
        self.btn_channel2.setGeometry(QtCore.QRect(50, 250, 75, 41))
        self.btn_channel2.setObjectName("btn_channel2")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_3.setGeometry(QtCore.QRect(180, 70, 211, 261))
        self.groupBox_3.setObjectName("groupBox_3")
        
        self.btn_move = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_move.setGeometry(QtCore.QRect(30, 80, 41, 31))
        self.btn_move.setObjectName("btn_move")
        self.btn_reset = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_reset.setGeometry(QtCore.QRect(30, 130, 41, 31))
        self.btn_reset.setObjectName("btn_reset")
        self.tb_move = QtWidgets.QLineEdit(self.groupBox_3)
        self.tb_move.setGeometry(QtCore.QRect(90, 89, 61, 21))
        self.tb_move.setObjectName("tb_move")
        self.label_7 = QtWidgets.QLabel(self.groupBox_3)
        self.label_7.setGeometry(QtCore.QRect(160, 90, 41, 16))
        self.label_7.setObjectName("label_7")
        self.btn_setspeed = QtWidgets.QPushButton(self.groupBox_3)
        self.btn_setspeed.setGeometry(QtCore.QRect(30, 180, 61, 31))
        self.btn_setspeed.setObjectName("btn_setspeed")
        
        self.tb_speed = QtWidgets.QLineEdit(self.groupBox_3)
        self.tb_speed.setGeometry(QtCore.QRect(110, 180, 61, 20))
        self.tb_speed.setObjectName("tb_speed")
        self.groupBox_4 = QtWidgets.QGroupBox(self.groupBox)
        self.groupBox_4.setGeometry(QtCore.QRect(440, 70, 181, 221))
        self.groupBox_4.setObjectName("groupBox_4")
        self.label_8 = QtWidgets.QLabel(self.groupBox_4)
        self.label_8.setGeometry(QtCore.QRect(30, 30, 54, 12))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox_4)
        self.label_9.setGeometry(QtCore.QRect(30, 90, 54, 12))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.groupBox_4)
        self.label_10.setGeometry(QtCore.QRect(30, 150, 54, 12))
        self.label_10.setObjectName("label_10")
        self.btn_radiotube1_on = QtWidgets.QPushButton(self.groupBox_4)
        self.btn_radiotube1_on.setGeometry(QtCore.QRect(30, 50, 51, 23))
        self.btn_radiotube1_on.setObjectName("btn_radiotube1_on")
        self.btn_radiotube1_off = QtWidgets.QPushButton(self.groupBox_4)
        self.btn_radiotube1_off.setGeometry(QtCore.QRect(90, 50, 51, 23))
        self.btn_radiotube1_off.setObjectName("btn_radiotube1_off")
        self.btn_radiotube2_on = QtWidgets.QPushButton(self.groupBox_4)
        self.btn_radiotube2_on.setGeometry(QtCore.QRect(30, 110, 51, 23))
        self.btn_radiotube2_on.setObjectName("btn_radiotube2_on")
        self.btn_radiotube2_0ff = QtWidgets.QPushButton(self.groupBox_4)
        self.btn_radiotube2_0ff.setGeometry(QtCore.QRect(90, 110, 51, 23))
        self.btn_radiotube2_0ff.setObjectName("btn_radiotube2_0ff")
        self.btn_value_on = QtWidgets.QPushButton(self.groupBox_4)
        self.btn_value_on.setGeometry(QtCore.QRect(30, 170, 51, 23))
        self.btn_value_on.setObjectName("btn_value_on")
        self.btn_value_off = QtWidgets.QPushButton(self.groupBox_4)
        self.btn_value_off.setGeometry(QtCore.QRect(90, 170, 51, 23))
        self.btn_value_off.setObjectName("btn_value_off")
        self.tb_infusion = QtWidgets.QLineEdit(self.groupBox)
        self.tb_infusion.setGeometry(QtCore.QRect(50, 100, 61, 20))
        self.tb_infusion.setObjectName("tb_infusion")
        self.tb_channel1 = QtWidgets.QLineEdit(self.groupBox)
        self.tb_channel1.setGeometry(QtCore.QRect(50, 210, 61, 20))
        self.tb_channel1.setObjectName("tb_channel1")
        self.tb_channel2 = QtWidgets.QLineEdit(self.groupBox)
        self.tb_channel2.setGeometry(QtCore.QRect(50, 310, 61, 20))
        self.tb_channel2.setObjectName("tb_channel2")
        self.btn_openserial = QtWidgets.QPushButton(MyWindow)
        self.btn_openserial.setGeometry(QtCore.QRect(50, 50, 75, 41))
        self.btn_openserial.setObjectName("btn_openserial")
        self.btn_closeserial = QtWidgets.QPushButton(MyWindow)
        self.btn_closeserial.setGeometry(QtCore.QRect(50, 100, 75, 41))
        self.btn_closeserial.setObjectName("btn_closeserial")
        self.groupBox_2 = QtWidgets.QGroupBox(MyWindow)
        self.groupBox_2.setGeometry(QtCore.QRect(200, 30, 371, 121))
        self.groupBox_2.setObjectName("groupBox_2")
        self.layoutWidget = QtWidgets.QWidget(self.groupBox_2)
        self.layoutWidget.setGeometry(QtCore.QRect(30, 30, 251, 76))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.label = QtWidgets.QLabel(self.layoutWidget)
        self.label.setObjectName("label")
        self.verticalLayout.addWidget(self.label)
        self.label_2 = QtWidgets.QLabel(self.layoutWidget)
        self.label_2.setObjectName("label_2")
        self.verticalLayout.addWidget(self.label_2)
        self.label_3 = QtWidgets.QLabel(self.layoutWidget)
        self.label_3.setObjectName("label_3")
        self.verticalLayout.addWidget(self.label_3)
        self.horizontalLayout.addLayout(self.verticalLayout)
        self.verticalLayout_2 = QtWidgets.QVBoxLayout()
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.tb_SerialName_injection = QtWidgets.QLineEdit(self.layoutWidget)
        self.tb_SerialName_injection.setObjectName("tb_SerialName_injection")
        self.tb_SerialName_injection.setText('/dev/cu.usbserial')
        self.verticalLayout_2.addWidget(self.tb_SerialName_injection)
        self.tb_SerialName_relay = QtWidgets.QLineEdit(self.layoutWidget)
        self.tb_SerialName_relay.setObjectName("tb_SerialName_relay")
        self.tb_SerialName_relay.setText('/dev/cu.usbserial-14330')
        self.verticalLayout_2.addWidget(self.tb_SerialName_relay)
        self.tb_SerialName_Ardunio = QtWidgets.QLineEdit(self.layoutWidget)
        self.tb_SerialName_Ardunio.setObjectName("tb_SerialName_Ardunio")
        self.tb_SerialName_Ardunio.setText('/dev/cu.usbserial-14310')
        self.verticalLayout_2.addWidget(self.tb_SerialName_Ardunio)
        self.horizontalLayout.addLayout(self.verticalLayout_2)
        self.horizontalLayout.setStretch(0, 1)
        self.horizontalLayout.setStretch(1, 3)

        self.retranslateUi(MyWindow)
        self.btn_openserial.clicked.connect(MyWindow.OpenSerial)
        self.btn_closeserial.clicked.connect(MyWindow.CloseSerial)
        self.btn_infusion.clicked.connect(MyWindow.Infusion)
        self.btn_channel1.clicked.connect(MyWindow.Channel1)
        self.btn_channel2.clicked.connect(MyWindow.Channel2)
        self.btn_move.clicked.connect(MyWindow.Move)
        self.btn_reset.clicked.connect(MyWindow.Reset)
        self.btn_radiotube1_on.clicked.connect(MyWindow.Radiotube1ON)
        self.btn_radiotube1_off.clicked.connect(MyWindow.Radiotube1OFF)
        self.btn_radiotube2_on.clicked.connect(MyWindow.Radiotube2ON)
        self.btn_radiotube2_0ff.clicked.connect(MyWindow.Radiotube2OFF)
        self.btn_value_on.clicked.connect(MyWindow.ValueON)
        self.btn_value_off.clicked.connect(MyWindow.ValueOFF)
        self.btn_setspeed.clicked.connect(MyWindow.SetSpeed)
        QtCore.QMetaObject.connectSlotsByName(MyWindow)
    def OpenSerial(self):
        pass
    def CloseSerial(self):
        pass
    def Infusion(self):
        pass
    def Channel1(self):
        pass
    def Channel2(self):
        pass
    def Move(self):
        pass
    def Reset(self):
        pass
    def Radiotube1ON(self):
        pass
    def Radiotube1OFF(self):
        pass
    def Radiotube2ON(self):
        pass
    def Radiotube2OFF(self):
        pass
    def ValueON(self):
        pass
    def ValueOFF(self):
        pass
    def SetSpeed(self):
        pass
    def retranslateUi(self, MyWindow):
        _translate = QtCore.QCoreApplication.translate
        MyWindow.setWindowTitle(_translate("MyWindow", "Form"))
        self.groupBox.setTitle(_translate("MyWindow", "控制指令"))
        self.btn_infusion.setText(_translate("MyWindow", "补液"))
        self.btn_channel1.setText(_translate("MyWindow", "通道1"))
        self.btn_channel2.setText(_translate("MyWindow", "通道2"))
        self.groupBox_3.setTitle(_translate("MyWindow", "注射器"))
        self.btn_move.setText(_translate("MyWindow", "移动"))
        self.btn_reset.setText(_translate("MyWindow", "复位"))
        self.label_7.setText(_translate("MyWindow", "ml"))
        self.btn_setspeed.setText(_translate("MyWindow", "设置速度"))
        self.groupBox_4.setTitle(_translate("MyWindow", "开关量"))
        self.label_8.setText(_translate("MyWindow", "电磁阀1"))
        self.label_9.setText(_translate("MyWindow", "电磁阀2"))
        self.label_10.setText(_translate("MyWindow", "两通阀"))
        self.btn_radiotube1_on.setText(_translate("MyWindow", "开"))
        self.btn_radiotube1_off.setText(_translate("MyWindow", "关"))
        self.btn_radiotube2_on.setText(_translate("MyWindow", "开"))
        self.btn_radiotube2_0ff.setText(_translate("MyWindow", "关"))
        self.btn_value_on.setText(_translate("MyWindow", "开"))
        self.btn_value_off.setText(_translate("MyWindow", "关"))
        self.btn_openserial.setText(_translate("MyWindow", "打开串口"))
        self.btn_closeserial.setText(_translate("MyWindow", "关闭串口"))
        self.groupBox_2.setTitle(_translate("MyWindow", "串口名"))
        self.label.setText(_translate("MyWindow", "注射器"))
        self.label_2.setText(_translate("MyWindow", "继电器"))
        self.label_3.setText(_translate("MyWindow", "Ardunio"))

