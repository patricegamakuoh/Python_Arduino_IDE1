'''servo control'''
from Arduino import Arduino
import time
board = Arduino(port="COM14")          #choose your COM port=" "

while 1:
     anglerange=[0,50,100,180]        #declare Angle range
     
     for angles in anglerange:         #for loop       
         board.Servos.attach(10)       #attach the desired digital pin attach(pin)
         board.Servos.write(10,angles) #write the angles to the servo write(pin,angle)
         time.sleep(0.6)               #delay in 1 seconds
         print(angles)                 #print the angles
  
      
