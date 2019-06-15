from PyQt5 import QtCore, QtGui, QtWidgets
from mywindow import Ui_MyWindow
import sys
from Serial import serialControl_inject,serialControl_Rtu,serialControl_Ardunio
import time
class myform(QtWidgets.QWidget,Ui_MyWindow):
    def __init__(self):
        super(myform,self).__init__()
        self.setupUi(self)
        self.btn_closeserial.setEnabled(False)
    def OpenSerial(self):
        injection_Serialname=self.tb_SerialName_injection.text()
        relay_Serialname=self.tb_SerialName_relay.text()
        Ardunio_Serialname=self.tb_SerialName_Ardunio.text()
        self.inject=serialControl_inject(injection_Serialname)
        self.relay=serialControl_Rtu(relay_Serialname)
        self.ardunio=serialControl_Ardunio(Ardunio_Serialname)
        if self.inject.isOpen and self.relay.isOpen and self.ardunio.isOpen:
            self.groupBox.setEnabled(True)
            self.btn_closeserial.setEnabled(True)
            self.btn_openserial.setEnabled(False)
    def CloseSerial(self):
        self.groupBox.setEnabled(False)
        self.btn_closeserial.setEnabled(False)
        self.btn_openserial.setEnabled(True)
    def Infusion(self):
        vol=int(self.tb_infusion.text())
        vol=abs(vol)
        self.relay.CloseRelay(0)
        self.relay.CloseRelay(1)
        self.ardunio.openRelay()
        time.sleep(0.5)
        self.inject.move(vol)
        time.sleep(0.5)
        self.ardunio.closeRelay()
    def Move(self):
        vol=int(self.tb_move.text())
        if vol<0:
            dire=1
        else:
            dire=0
        vol=abs(vol)
        self.inject.move(vol,dire)
    def Channel1(self):
        vol=int(self.tb_channel1.text())
        vol=abs(vol)
        self.ardunio.closeRelay()
        self.relay.OpenRelay(0)
        time.sleep(0.5)
        self.relay.CloseRelay(1)
        time.sleep(0.5)
        self.inject.move(vol,1)
    def Channel2(self):
        vol=int(self.tb_channel2.text())
        vol=abs(vol)
        self.ardunio.closeRelay()
        self.relay.OpenRelay(1)
        time.sleep(0.5)
        self.relay.CloseRelay(0)
        time.sleep(0.5)
        self.inject.move(vol,1)
    def SetSpeed(self):
        speed=int(self.tb_speed.text())
        speed=abs(speed)
        self.inject.setSpeed(speed)
    def Reset(self):
        self.inject.reset()
    def Radiotube1ON(self):
        self.relay.OpenRelay(0)
    def Radiotube1OFF(self):
        self.relay.CloseRelay(0)
    def Radiotube2ON(self):
        self.relay.OpenRelay(1)
    def Radiotube2OFF(self):
        self.relay.CloseRelay(1)
    def ValueON(self):
        self.ardunio.openRelay()
    def ValueOFF(self):
        self.ardunio.closeRelay()
app=QtWidgets.QApplication(sys.argv)
mywindow=myform()
mywindow.show()
app.exec_()
sys.exit()
