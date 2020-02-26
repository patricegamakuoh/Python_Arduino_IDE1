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
board = Arduino(port="COM14")                  #Create an object for the Serial port. Adjust 'com11' to whatever port your arduino is sending to.
measuringRod = cylinder( radius= .1, length=6, pos=vector(-3,-2,0))
lengthLabel = label(pos=vector(0,3,0), text='Target Distance is: ', box=False, height=40)
target=box(pos=vector(0,-.5,0), length=.2, width=3, height=3, color=color.blue)

while True :                                   #Create a loop that continues to read and display the data
    rate(3/dt)                                 #Tell vpython to run this loop 20 times a second
    myData = str(board.Distance_Sense(13,11))  #Check to see if a data point 
    #print(myData) #Print the measurement to confirm things are working
    distance = float(myData)                   #convert reading to a floating point number
    print (distance)                           #Print the measurement to confirm things are working   
    #measuringRod.length=distance              #Change the length of your measuring rod to your last measurement
    target.pos=vector(-3+distance,-.5,0)
    myLabel= 'Target Distance is: ' + myData   #Create label by appending string myData to string
    lengthLabel.text = myLabel                 #display updated myLabel on your graphic
    t = t+dt