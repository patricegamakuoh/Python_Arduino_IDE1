'''颜色探测：探测视野中有无设定颜色'''
from Arduino import Arduino

import time

board = Arduino("9600",port="COM3",timeout=0.5)


#开启MU
while  1:
       mu=board.muBegin("VISION_COLOR_DETECT")
       if mu==1:
          print("Mu Sensor is Ok")  
          break
while  1:
       mu=board.muVisionColorSet("MU_COLOR_PURPLE")#指定探测颜色，包括：黑色-BLACK;白色-WHITE;红色-RED；黄-YELLOW;
                                                   #绿-GREEN;青色-CYAN;蓝色-BLUE;紫色-PURPLE
       if mu:
          print("Color setting is Ok")  
          print(mu)
          break

while 1:     
            
       muvalue = board.muGetValue("VISION_COLOR_DETECT")
       if muvalue:
   
            print(muvalue)
     
  
board.close()
   
