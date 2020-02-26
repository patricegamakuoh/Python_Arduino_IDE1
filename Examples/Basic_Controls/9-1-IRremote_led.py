'''红外控制LED'''
from Arduino import Arduino
import time

board = Arduino( port="COM3")

def led_on():
    board.digitalWrite(12,'HIGH')
  
   
def led_off():
     board.digitalWrite(12,'LOW')
    
    
while board.pinMode(12, "OUTPUT")!=1:#LED接12pin
    board.pinMode(12, "OUTPUT")


while 1:
      IRflag=board.IRstart(11)#红外接收传感器只能连接到11脚
     
      if IRflag==1:
           
            print("Start")
            break
                                              
while 1:
    IRvalue=board.IRrecv()
    if IRvalue=="FF30CF":#按钮1
         print(IRvalue)
         led_on()
    elif IRvalue=="FF6897":#按钮0
         print(IRvalue)
         led_off()
 
board.close()
