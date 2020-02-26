from Arduino import Arduino
import time

'''马达程序，5S后自动停止 '''

board = Arduino(port="COM3")#com口根据实际情况修改

while board.pinMode(6, "OUTPUT")!=1:#定义6pin为输出，马达一端连6pin，另一端连GND
    board.pinMode(6, "OUTPUT")
   
board.digitalWrite(6,'HIGH')

time.sleep(5)
  
    
board.digitalWrite(6,'LOW')
   

