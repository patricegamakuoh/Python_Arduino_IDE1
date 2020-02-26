#绘制创意几何图案
import turtle

def drawSpiral(t, angle):
    ''' takes a turtle, t, and an angle in degrees '''
    length = 1
    for i in range(84):
        t.forward(length)
        t.right(angle)
        length = length + 2


wn = turtle.Screen()       # Set up the window and its attributes
wn.bgcolor("lightyellow")

turing = turtle.Turtle()    # create turing
turing.color('red')
turing.speed(0)

## draw the first spiral ##
# position turing

turing.penup()

turing.backward(200)
turing.pendown()

# draw the spiral using a 90 degree turn angle
drawSpiral(turing, 90)


## draw the second spiral ##
# position turing

turing.penup()
turing.home()
turing.forward(90)
turing.pendown()

drawSpiral(turing, 88)

wn.exitonclick()