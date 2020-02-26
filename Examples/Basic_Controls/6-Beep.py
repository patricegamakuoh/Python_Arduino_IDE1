'''蜂鸣器程序'''
from Arduino import Arduino

import time


board = Arduino(port="COM3")


while board.pinMode(9, "OUTPUT")!=1:#定义9脚为输出
      board.pinMode(9, "OUTPUT")

board.tone(9,330,200)
board.tone(9,350,200)
board.tone(9,393,200)

time.sleep(1)
board.notone(9)
 
