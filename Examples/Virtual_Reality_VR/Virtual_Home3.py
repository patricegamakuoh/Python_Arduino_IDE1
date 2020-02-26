'''NOTE! before using this program, make sure you have vPthon7 runing or already installed on your computer,
if not open your comand prompt then Enter: pip install vpython '''

#Import all the vPython library
from vpython import *                          
from Arduino import Arduino

scene.width = 1000
scene.height = 600
scene.range = 1.3
scene.title = "Virtual Reality VR demo"
dt = 0.0002
t = 0
side = 4.0
thk = 0.3
s2 = 2*side - thk
s3 = 2*side + thk
board = Arduino(port="COM14")                  #Create an object for the Serial port. Adjust 'com11' to whatever port your arduino is sending to.
#measuringRod = cylinder( radius= .1, length=6, pos=vector(-3,-2,0))
#lengthLabel = label(pos=vector(0,3,0), text='Target Distance is: ', box=False, height=40)
#target=box(pos=vector(0,-.5,0), length=.2, width=3, height=3, color=color.blue)
box(length=.100, width=15,height=1, pos=vector(-9.5,0,0),color=color.blue) 
box (pos=vector(-14.5, 0, 4), size=vector(s3, thk, s3),  color = color.red)
sphere(pos=vector(-12.5, 0, -4),size=vector(s3, thk, s3),color=color.yellow, radius=2.2)
box(pos=vector(-9,0,9), size=vector(3, 5, -3),color=color.yellow)

target=box(length=.1, width=10,height=5, pos=vector(-6,0,0),color=color.blue)     #Create the object that will represent your target (which is a colored card for our project)
myBoxEnd=box(length=.1, width=10,height=5, pos=vector(-8.5,0,0),color=color.blue) #This object is the little square that is the back of the ultrasonic sensor
myTube2=cylinder(pos=vector(-8.5,0,-2.5), radius=1.5,length=2.5 )   #One of the 'tubes' in the front of the ultrasonic sensor
myTube3=cylinder(pos=vector(-8.5,0,2.5), radius=1.5,length=2.5 )    #Other tube
myBall=sphere(color=color.yellow,size=vector(s3, thk, s3), radius=.4)
while True :                                   #Create a loop that continues to read and display the data
    rate(3/dt)                                 #Tell vpython to run this loop 20 times a second
    myData = str(board.Distance_Sense(13,11))  #Check to see if a data point 
    #print (myData) #Print the measurement to confirm things are working
    distance = float(myData)                   #convert reading to a floating point number
    print (distance)                           #Print the measurement to confirm things are working   
    target.pos=vector(-3+distance,-.5,0)
    #myLabel= 'Target Distance is: ' + myData   #Create label by appending string myData to string
    #lengthLabel.text = myLabel                 #display updated myLabel on your graphic
    #target.pos=vector(-6 + distance,0,0)   
    t = t+dt
