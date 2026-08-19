import turtle
import time
import math

screen = turtle.Screen()
screen.setup(700,700)
screen.bgcolor("green")
screen.title("Practice")

turtle.tracer(0)

axis = turtle.Turtle()
axis.hideturtle()
axis.speed(0)
axis.color("red")

axis.penup()
axis.goto(-300,0)
axis.pendown()
axis.goto(300,0)

axis.penup()
axis.goto(0,300)
axis.pendown()
axis.goto(0,-300)


t = turtle.Turtle()
t.speed(0)
t.hideturtle()
t.penup()

x1,y1,x2,y2 = -100,-100,200,100

dx = abs(x2-x1)
dy = abs(y2-y1) 

sx = 1 if x1<x2 else -1
sy = 1 if y1<y2 else -1
x,y=x1,y1

if dx>=dy:
    p = 2*dy-dx
    while True:
        t.goto(x,y)
        t.dot(6,"blue")
        turtle.update()
        time.sleep(0.03)
        if x == x2:
            break
        x+=sx
        if p<0:
            p += 2*dy 
        else:
            p += 2*(dy-dx)
            y+=sy


else:
    p = 2*dx-dy
    while True:
        t.goto(x,y)
        t.dot(6,"blue")
        turtle.update()
        time.sleep(0.03)
        if y==y2:
            break
        y+=sy
        if p<0:
            p+=2*dx
        else:
            p+=2*(dx-dy)
            x+=sx
            
turtle.done()