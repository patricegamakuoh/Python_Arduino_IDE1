# 用turtle绘制艺术四边形
#for循环的应用
import turtle

wn = turtle.Screen()
wn.bgcolor("light yellow")
turing = turtle.Turtle()

turing.speed(0)
def drawSquare(someTurtle):
    for i in range(4):
        someTurtle.forward(200)
        someTurtle.right(90)

def drawArt():
    turing.color("red")
    turing.pensize(2)
    for i in range(1, 37):
        drawSquare(turing)
        turing.right(10)


drawArt()
wn.exitonclick()
