from Arduino import Arduino
import time

'''distance sensor control led brightness '''

def my_map(x, in_min, in_max, out_min, out_max):  
    return int((x-in_min) * (out_max-out_min) / (in_max-in_min) + out_min)

board = Arduino(port="COM14")            #com口根据实际情况修改
while True:
      value = board.Distance_Sense(13,11)#Distance_Sense(trig_pin,echo_pin)
      if value:
         value=my_map(int(value), 0, 50,0,180)
         board.analogWrite(3, value)
         #time.sleep(0.6)                 #Delay for some time            
         print (value)
         #time.sleep(0.07)                #Delay for some time
