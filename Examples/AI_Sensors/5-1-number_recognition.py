''' 卡片识别程序，''' 
from Arduino import Arduino



board = Arduino(port="COM3")#com口根据实际情况修改


#开启MU
while  1:
         mu=board.muBegin("VISION_NUM_CARD_DETECT")#数字卡片识别，可更换识别类型，具体使用见说明文档
         if mu==1:
            print("Mu Sensor is Ok")  
            break

while 1:     
            
       muvalue = board.muGetValue("VISION_NUM_CARD_DETECT")
       if muvalue: 
          print(muvalue)
     
       
     

   



