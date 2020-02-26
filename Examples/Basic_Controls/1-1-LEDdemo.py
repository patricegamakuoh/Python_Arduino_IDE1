#!/usr/bin/env python
from Arduino import Arduino
import time

def Blink(led_pin,port="COM14"):
    """
    Blinks an LED in 1 sec intervals
    """
    board = Arduino(port=port)                #com口根据实际情况修改
    while board.pinMode(led_pin, "OUTPUT")!=1:#定义13脚为输出，控制LED亮灭
          board.pinMode(led_pin, "OUTPUT") 
    while True:  
        board.digitalWrite(led_pin, "LOW")
        print('LED_OFF')
        time.sleep(1)
        board.digitalWrite(led_pin, "HIGH")
        print('LED_ON')
        time.sleep(1)

def my_map(x,in_min,in_max,out_min,out_max): 
    return int((x-in_min) * (out_max-out_min) / (in_max-in_min) + out_min) 
       
def softBlink(led_pin,port="COM14"):
    """
    Fades an LED off and on, using
    Arduino's analogWrite (PWM) function
    """
    board = Arduino(port=port)
    while board.pinMode(led_pin, "OUTPUT")!=1:#定义13脚为输出，控制LED亮灭
          board.pinMode(led_pin, "OUTPUT") 
    i = 0
    while True:
        i += 1
        k = i % 510
        if k % 5 == 0:
            if k > 255:
                k = 510 - k
            board.analogWrite(led_pin, k)

def adjustBrightness(pot_pin, led_pin,port="COM14"):
    """
    Adjusts brightness of an LED using a
    potentiometer.
    """
    board = Arduino(port=port)
    while board.pinMode(led_pin, "OUTPUT")!=1:#定义13脚为输出，控制LED亮灭
          board.pinMode(led_pin, "OUTPUT")
    while True:
        time.sleep(0.01)
        val = board.analogRead(pot_pin) 
        val = my_map(val,0,1023,0,255)        #Map values from the sensor to any desired value
        print(val)
        board.analogWrite(led_pin, val)

'''THE MAIN LOOP WHERE YOU RUN YOUR CODE '''            
if __name__ == "__main__":
 '''Uncomment and run your code here '''
      #Blink(3)                        #blink LED in Pin 3...change the pins as you want!
       softBlink(3)                    #fade LED in PWM Pin 3...change the pins as you want!
      #adjustBrightness('A0',3)        #Ajust LED brigthness in Pin 3...change the pins as you want!
