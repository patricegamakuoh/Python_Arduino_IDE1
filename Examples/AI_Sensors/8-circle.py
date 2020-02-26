'''画圆'''
import turtle
    
import time

 
def describing_circle(radii):

    #页面的大小

    turtle.setup(width=800, height=400)
   

    #颜色

    turtle.color('blue','red')

    #笔粗细

    turtle.pensize(3)


    turtle.Turtle().screen.delay(1)#设置速度 


    turtle.circle(radii)
   


describing_circle(100)#画半径100的圆
 
window=turtle.Screen()
window.exitonclick()
time.sleep(1)


