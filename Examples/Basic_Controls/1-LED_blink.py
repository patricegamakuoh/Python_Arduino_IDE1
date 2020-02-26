from Arduino import Arduino
import time
'''LED闪烁程序 '''

board = Arduino(port="COM14")#com口根据实际情况修改

while board.pinMode(13, "OUTPUT")!=1:#定义13脚为输出，控制LED亮灭
      board.pinMode(13, "OUTPUT")
   
while True:
    
    board.digitalWrite(13, "LOW")
    print('LED_OFF')
    time.sleep(1)
    
    board.digitalWrite(13, "HIGH")
    print('LED_ON')
    time.sleep(1)
