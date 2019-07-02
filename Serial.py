import SendConmand
import serial
import time
import ModbusRtu
import Ardunio_conmand
class serialControl_inject:
    def __init__(self,portname,baudrate=9600):
        self.serial=serial.Serial(portname,baudrate)
        self.isOpen=self.serial.isOpen()
        #self.reset()
        self.totalLength=0
    def OnlyMove(self,vol,direction=0):
        movelength=vol*24.88/20
        myvol=vol
        conmand=SendConmand.Move(myvol,direction)
        self.serial.write(conmand)
    # 移动注射阀，vol为体积，direction为方向，0代表抽溶剂
    def move(self,vol,direction=0):
        movelength=vol*24.88/20
        myvol=vol
        if movelength+self.totalLength>30:
            movelength=30-self.totalLength
            myvol=movelength*20/24.88
        conmand=SendConmand.baseConmand(SendConmand.GET_CURRENT_POSITION)
        self.serial.write(conmand)
        a=self.serial.read(8)[3:5]
        pos1=int.from_bytes(a, byteorder='little', signed=True)
        #print(pos1)
        conmand=SendConmand.Move(myvol,direction)
        self.serial.write(conmand)
        self.serial.read(8)
        conmand=SendConmand.baseConmand(SendConmand.GET_CURRENT_POSITION)
        self.serial.write(conmand)
        a=self.serial.read(8)[3:5]
        pos2=int.from_bytes(a, byteorder='little', signed=True)
        #print(pos2)
        distance=abs(pos2-pos1)*24.88/9952
        self.totalLength=self.getPosition()
        return distance
    def reset(self):
        conmand=SendConmand.baseConmand(SendConmand.RESET)
        self.serial.write(conmand)
        self.serial.read(8)
        conmand=SendConmand.baseConmand(SendConmand.CLEAR_POSITION)
        self.serial.write(conmand)
        self.serial.read(8)
        conmand=SendConmand.baseConmand(SendConmand.GET_CURRENT_POSITION)
        self.serial.write(conmand)
        a=self.serial.read(8)[3:5]
        pos2=int.from_bytes(a, byteorder='little', signed=True)
        return pos2
    def getPosition(self):
        conmand=SendConmand.baseConmand(SendConmand.GET_CURRENT_POSITION)
        self.serial.write(conmand)
        a=self.serial.read(8)[3:5]
        pos2=int.from_bytes(a, byteorder='little', signed=True)
        return pos2*24.88/9952
    def setSpeed(self,speed):
        conmand=SendConmand.setCurrentSpeed(speed)
        self.serial.write(conmand)
        self.serial.read(8)
        conmand=SendConmand.baseConmand(SendConmand.GET_MAX_SPEED)
        self.serial.write(conmand)
        a=self.serial.read(8)[3:5]
        myspeed=int.from_bytes(a, byteorder='little', signed=True)
        return myspeed
    def setDefaultSpeed(self,speed):
        conmand=SendConmand.setMaxSpeed(speed)
        self.serial.write(conmand)
        self.serial.read(8)
        conmand=SendConmand.baseConmand(SendConmand.GET_MAX_SPEED)
        self.serial.write(conmand)
        a=self.serial.read(8)[3:5]
        myspeed=int.from_bytes(a, byteorder='little', signed=True)
        return myspeed
class serialControl_Rtu:
    def __init__(self,portname,baudrate=9600):
        self.serial=serial.Serial(portname,baudrate)
        self.isOpen=self.serial.isOpen()
    def OpenRelay(self,channel):
        byte=ModbusRtu.OpenRelay(channel)
        self.serial.write(byte)
    def CloseRelay(self,channel):
        byte=ModbusRtu.CloseRelay(channel)
        self.serial.write(byte)
class serialControl_Ardunio:
    def __init__(self,portname,baudrate=9600):
        self.serial=serial.Serial(portname,baudrate)
        self.isOpen=self.serial.isOpen()
    def openRelay0(self):
        byte=Ardunio_conmand.OpenRelay0()
        self.serial.write(byte)
    def closeRelay0(self):
        byte=Ardunio_conmand.CloseRelay0()
        self.serial.write(byte)
    def openRelay1(self):
        byte=Ardunio_conmand.OpenRelay1()
        self.serial.write(byte)
    def closeRelay1(self):
        byte=Ardunio_conmand.CloseRelay1()
        self.serial.write(byte)
    def openRelay2(self):
        byte=Ardunio_conmand.OpenRelay2()
        self.serial.write(byte)
    def closeRelay2(self):
        byte=Ardunio_conmand.CloseRelay2()
        self.serial.write(byte)
if __name__=='__main__':
    s=serialControl_inject('/dev/cu.usbserial')
    '''s1=serial.Serial('/dev/cu.usbserial-14430',9600)
    on=bytes('o',encoding='utf-8')
    off=bytes('f',encoding='utf-8')
    s1.write(on)
    time.sleep(1)'''
    #a=s.setSpeed(50)
    a=s.move(10,0)
    '''time.sleep(0.5)
    s1.write(off)'''
    print(a)

