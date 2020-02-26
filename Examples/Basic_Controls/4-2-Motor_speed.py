from Arduino import Arduino
import time
i=100

'''马达加速程序，加速到最大速度后停止'''

board = Arduino(port="COM3")#com口根据实际情况修改

while board.pinMode(6, "OUTPUT")!=1:#定义6pin为输出，马达一端连6pin，另一端连GND
    board.pinMode(6, "OUTPUT")
   


while i<255: 
  board.analogWrite(6,i)
  time.sleep(0.1)
  i=i+1
    
board.digitalWrite(6,'LOW')
time.sleep(1)
