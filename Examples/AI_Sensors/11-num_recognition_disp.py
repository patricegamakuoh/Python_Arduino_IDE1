''' 数字卡片识别显示程序，''' 
from Arduino import Arduino

import time

board = Arduino(port="COM13")#com口根据实际情况修改


#开启图像识别传感器
while  1:
         mu=board.muBegin("VISION_NUM_CARD_DETECT")#数字卡片识别，可更换识别类型，具体使用见说明文档
         if mu==1:
            print("Mu Sensor is Ok")  
            break
#开启点阵屏
while  1:
         led=board.LatticeLED.start(8,7)#8：CLK_PIN;7:SDA_PIN
         if led==1:
            print("LatticeLED is Ok")  
            break
        
while 1:     
            
       muvalue = board.muGetValue("VISION_NUM_CARD_DETECT")
       if muvalue:         
          board.LatticeLED.display(muvalue)#点阵屏显示识别到的数字
         # time.sleep(3)
          #print(muvalue) 
