from Arduino import Arduino

import time
'''触碰开关程序 '''


board = Arduino(port="COM3")#com口根据实际情况修改

while board.pinMode(9, "INPUT")!=1:#定义9脚为输入，触碰开关信号线连到9pin
      board.pinMode(9, "INPUT")
    

while 1:
   print( board.digitalRead(9))
   
