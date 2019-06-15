#baseConmand（conmand）：基本控制指令，接收一个参数作为控制行为
#  conmand：RESET，复位
#           STOP，急停
#          GET_MOTOR_STATE，查询电机状态
#          GET_CURRENT_POSITION，查询当前位置
#          CLEAR_POSITION，清除位置
#          GET_DIRECTION，查询活塞运动方向
#          GET_MAX_SPEED,查询最大速度
#          GET_RESET_SPEED，查询复位速度
#          GET_IS_RESET，查询上电复位
#          GET_BAUDRATE，查询波特率

#Move(vol,direction=0)：运动控制指令
# vol，表示排（抽）多少ml溶剂
# direction，表示运动方向，0代表抽，1代表排

#setMaxSpeed(speed)：永久设定最大速度
# speed代表速度值，范围为5-350r/min

#setCurrentSpeed(speed):临时设定最大速度，断电后恢复原最大速度
# speed代表速度值，范围为5-350r/min

#getStopEvent():获取停止事件

#isReset(reset=False):上电是否复位
b0=0xcc
b1=0x00
#b5=0xdd
b11=0xdd
default_b=0x00

RESET=0
STOP=1
GET_MOTOR_STATE=2
GET_CURRENT_POSITION=3
CLEAR_POSITION=4
GET_DIRECTION=5
GET_MAX_SPEED=6
GET_RESET_SPEED=7
GET_IS_RESET=8
GET_BAUDRATE=9
def _int_to_byte(myint):
    tmp=myint.to_bytes(4,byteorder='little')
    return tmp[0],tmp[1]
def _getb6andb7(b0,b1,b2,b3,b4,b5):
    tmp=b0+b1+b2+b3+b4+b5
    byte=tmp.to_bytes(4,byteorder='little')
    return byte[0],byte[1]
def _getb12andb13(b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11):
    tmp=b0+b1+b2+b3+b4+b5+b6+b7+b8+b9+b10+b11
    byte=tmp.to_bytes(4,byteorder='little')
    return byte[0],byte[1]

def baseConmand(conmand=RESET):
    if conmand==RESET:
        b2=0x45
    elif conmand==STOP:
        b2=0x49
    elif conmand==GET_MOTOR_STATE:
        b2=0x4a
    elif conmand==GET_CURRENT_POSITION:
        b2=0x66
    elif conmand==CLEAR_POSITION:
        b2=0x67
    elif conmand==GET_DIRECTION:
        b2=0x68
    elif conmand==GET_MAX_SPEED:
        b2=0x27
    elif conmand==GET_RESET_SPEED:
        b2=0x2b
    elif conmand==GET_IS_RESET:
        b2=0x2e
    elif conmand==GET_BAUDRATE:
        b2=0x21
    b3=0x00
    b4=0x00
    b5=0xdd
    b6,b7=_getb6andb7(b0,b1,b2,b3,b4,b5)
    return [b0,b1,b2,b3,b4,b5,b6,b7]
def Move(vol,direction=0):
    #vol代表容量,单位ml
    #direction,0代表抽液，1代表排液
    if direction==0:
        b2=0x41
    else:
        b2=0x42
    st=int(vol/0.0020096)
    b3,b4=_int_to_byte(st)
    b5=0xdd
    b6,b7=_getb6andb7(b0,b1,b2,b3,b4,b5)
    return [b0,b1,b2,b3,b4,b5,b6,b7]
def setMaxSpeed(speed):
    myspeed=speed
    b2=0x07
    b3=0xff
    b4=0xee
    b5=0xbb
    b6=0xaa
    if myspeed<5 or myspeed>350:
        myspeed=200
    b7,b8=_int_to_byte(myspeed)
    b9=default_b
    b10=default_b
    b12,b13=_getb12andb13(b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11)
    return [b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13]
def setCurrentSpeed(speed):
    myspeed=speed
    b2=0x4b
    if myspeed<1 or myspeed>350:
        return
    b3,b4=_int_to_byte(myspeed)
    b5=0xdd
    b6,b7=_getb6andb7(b0,b1,b2,b3,b4,b5)
    return [b0,b1,b2,b3,b4,b5,b6,b7]
def getStopEvent():
    b2=0x65
    b3=0x01
    b4=0x00
    b5=0xdd
    b6,b7=_getb6andb7(b0,b1,b2,b3,b4,b5)
    return [b0,b1,b2,b3,b4,b5,b6,b7]
def isReset(reset=False):
    b2=0x0e
    b3=0xff
    b4=0xee
    b5=0xbb
    b6=0xaa
    if reset:
        b7=0x01
    else:
        b7=0x00
    b8=0x00
    b9=0x00
    b10=0x00
    b12,b13=_getb12andb13(b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11)
    return [b0,b1,b2,b3,b4,b5,b6,b7,b8,b9,b10,b11,b12,b13]
if __name__=='__main__':
    import serial
    s=serial.Serial('/dev/cu.usbserial-14110',9600)
    #conmand=baseConmand(GET_DIRECTION)
    #conmand=baseConmand(RESET)
    #conmand=Move(10,0)
    #conmand=setMaxSpeed(100)
    #conmand=setCurrentSpeed(20)
    conmand=isReset(False)
    s.write(conmand)
    a=s.read(8)
    data_int = int.from_bytes(a, byteorder='little', signed=True)
    print(a[3])
    print(data_int)
