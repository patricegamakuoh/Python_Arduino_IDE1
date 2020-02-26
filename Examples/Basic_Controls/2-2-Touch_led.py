from Arduino import Arduino

import time
'''触碰开关控制LED亮灭程序 '''

board = Arduino(port="COM3")#com口根据实际情况修改

while board.pinMode(9, "INPUT")!=1:#定义9脚为输入，触碰开关信号线连到9pin
    board.pinMode(9, "INPUT")

while board.pinMode(13, "OUTPUT")!=1:#定义13脚为输出，控制LED亮灭，
      board.pinMode(13, "OUTPUT")   

while 1:
    value=board.digitalRead(9)
    if value==1:#开关没按下
        board.digitalWrite(13, "LOW")
    elif value==0:#按下开关
        board.digitalWrite(13, "HIGH")
