''' 球体识别程序，只能识别网球和乒乓球''' 
from Arduino import Arduino


board = Arduino(port="COM13")#com口根据实际情况修改


#开启MU
while  1:
       mu=board.muBegin("VISION_BALL_DETECT")
       if mu==1:
          print("Mu Sensor is Ok")  
          break

while 1:     
            
       muvalue = board.muGetValue("VISION_BALL_DETECT")
       if muvalue:
          print(muvalue)
     
  
board.close()
   
