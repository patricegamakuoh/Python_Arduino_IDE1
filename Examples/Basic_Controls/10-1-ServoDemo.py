from Arduino import Arduino
import time

port="COM14" #Change the COMport

'''Defined functions here'''
def ServoSweep(ServoPin):
    """
    从 o 扫描伺服到 180 和回
    Sweep Servo from o to 180 and back 
    """
    board = Arduino(port=port)
    while True:
        board.Servos.attach(ServoPin)    #attach the servo pin     
        board.Servos.write(ServoPin,0)   #write (servoPin,Angle) 
        time.sleep(1)
        board.Servos.attach(ServoPin)    #attach the servo pin 
        board.Servos.write(ServoPin,180) #write (servoPin,Angle)  
        time.sleep(1)
        board.Servos.detach(ServoPin)    #free pin 9
        #print (board.Servos.read(9))    #should be 0

def my_map(x, in_min, in_max, out_min, out_max):  
    return int((x-in_min) * (out_max-out_min) / (in_max-in_min) + out_min)

def adjustServoAngle(pot_pin,servo_pin):
    """
    使用电位计调整伺服角度
    Adjusts adjustServoAngle using a
    potentiometer.
    """
    board = Arduino(port=port)
    while True:        
        val = board.analogRead(pot_pin)
        val = my_map(val,0,1023,0,180)       #Map potentiometer values to 0-180 degree 
        print(val)
        board.Servos.attach(servo_pin)       #attach the servo pin 
        board.Servos.write(servo_pin,val)    #write (servoPin,Angle)
        #board.Servos.writeMicroseconds(9,10)
    
'''THE MAIN LOOP WHERE YOU RUN YOUR CODE'''
if __name__ == "__main__":
       adjustServoAngle('A0',10)   #require potentiometer pin and adjustServoAngle(analogPin,Pin)
      #ServoSweep(10)              #require ServoSweep(Pin)
     
     
