''' 颜色识别，可识别颜色种类：
（1）黑色；（2）白色；（3）红色；（4）黄色；（5）绿色；（6）青色；（7）蓝色；（8）紫色'''
from Arduino import Arduino

import time

board = Arduino(port="COM14")


#开启MU
while  1:
       mu=board.muBegin("VISION_COLOR_RECOGNITION")
       if mu==1:
          print("Mu Sensor is Ok")  
          break

while 1:     
            
       muvalue = board.muGetValue("VISION_COLOR_RECOGNITION")
       if muvalue:
   
           print(muvalue)
      

   
