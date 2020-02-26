''' 人体头像识别程序，需要面部正对摄像头，只能识别有没有人''' 
from Arduino import Arduino

import time

board = Arduino(port="COM13")


#开启MU
while  1:
       mu=board.muBegin("VISION_BODY_DETECT")
       if mu==1:
          print("Mu Sensor is Ok")  
          break

while 1:     
            
       muvalue = board.muGetValue("VISION_BODY_DETECT")
       if muvalue:
   
           print(muvalue)
     
  
board.close()
