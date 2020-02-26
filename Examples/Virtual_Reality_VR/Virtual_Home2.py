'''NOTE! before using this program, make sure you have vPthon7 runing or already installed on your computer,
if not open your comand prompt then Enter: pip install vpython '''

from vpython import *            #Import all the vPython library
from Arduino import Arduino
import time
scene.width = 800
scene.height = 600
scene.range = 1.2                #Set range of your scene to be 12 inches by 12 inches by 12 inches. 
scene.title = "Virtual Reality2 VR demo"

#side = 4.0
#thk = 0.3
#s2 = 2*side - thk
#s3 = 2*side + thk

target=box(length=.1, width=10,height=5, pos=vector(-6,0,0),color=color.blue)     #Create the object that will represent your target (which is a colored card for our project)
myBoxEnd=box(length=.1, width=10,height=5, pos=vector(-8.5,0,0),color=color.blue) #This object is the little square that is the back of the ultrasonic sensor
myTube2=cylinder(pos=vector(-8.5,0,-2.5), radius=1.5,length=2.5 )   #One of the 'tubes' in the front of the ultrasonic sensor
myTube3=cylinder(pos=vector(-8.5,0,2.5), radius=1.5,length=2.5 )    #Other tube
myBall=sphere(color=color.yellow, radius=.4)
#box(length=.100, width=15,height=1, pos=vector(-9.5,0,0),color=color.blue) 
#box (pos=vector(-14.5, 0, 4), size=vector(s3, thk, s3),  color = color.red)
#sphere(pos=vector(-12.5, 0, -4),size=vector(s3, thk, s3),color=color.yellow, radius=2.2)
#box(pos=vector(-9,0,9), size=vector(3, 5, -3),color=color.yellow)
dt = 0.0002
t = 0
board = Arduino(port="COM14")#Create sensorData object to read serial port data coming from arduino

while True:                  #This is a while loop that will loop forever, since True is always True.   
    rate(30)               #We need to tell Vpython how fast to go through the loop. 25 times a second works pretty well
    #rate(3/dt) 
    textline = str(board.Distance_Sense(13,11)) #textline= sensorData.readline()     # read the entire line of text
    #print(textline)
    # dataNums=textline.split(',')       #Remember to split the line of text into an array at the commas
    # red=float(dataNums[0])             #Make variables for Red, Blue, Green. Remember
    # green=float(dataNums[1])           #the array was read as text, so must be converted
    # blue=float(dataNums[2])            #to numbers with float command
    float(textline)                 #last number in the list is the distance
    print (textline)
    #blue=blue*.7                                  #On my sensor, blue is always a little too strong, so I tone it down a little
    #if (dist>=1.5 and dist<=2.25):                #only change color or target if target is between 1.5 and 2.25 inches from sensor
    #target.color=(red/255., green/255., blue/255.)#This keeps color from flickering.
    target.pos=vector(-6 + textline,0,0)           #Adjust the position of the target object to match the distance of the real target from the real sensor
    #t = t+dt
