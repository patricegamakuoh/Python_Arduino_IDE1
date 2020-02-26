'''红外遥控马达'''
from Arduino import Arduino
import time

board = Arduino(port="COM13")

def motorrun():
    board.digitalWrite(6,'HIGH')
  
   
def motorstop():
     board.digitalWrite(6,'LOW')
    
    
while board.pinMode(6, "OUTPUT")!=1:#马达一端接6pin，一端接GND
    board.pinMode(6, "OUTPUT")

while 1:
      IRflag=board.IRstart(11)#红外信号线只能接11pin
     
      if IRflag==1:
           
            print("Start")
            break
                                              
while 1:
    IRvalue=board.IRrecv()
    if IRvalue=="FF30CF":#按钮1
         print(IRvalue)
         motorrun()
    elif IRvalue=="FF6897":#按钮0
         print(IRvalue)
         motorstop()
 
board.close()
