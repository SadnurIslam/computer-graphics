import turtle
import time

# Screen
turtle.setup(700, 700)
turtle.bgcolor("white")
turtle.title("DDA Line Drawing Algorithm")
turtle.tracer(0)

# -------- Draw Axes --------
axis = turtle.Turtle()
axis.hideturtle()
axis.speed(0)
axis.color("gray")

# X-axis
axis.penup()
axis.goto(-300, 0)
axis.pendown()
axis.goto(300, 0)

# Y-axis
axis.penup()
axis.goto(0, -300)
axis.pendown()
axis.goto(0, 300)

# Labels
axis.penup()
axis.goto(285, -15)
axis.write("X")
axis.goto(10, 285)
axis.write("Y")

# -------- Drawing Turtle --------
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()

# Input
x1 = 200
y1 = -200
x2 = 0
y2 = 500

# Draw ideal line (reference)
ref = turtle.Turtle()
ref.hideturtle()
ref.speed(0)
ref.color("lightgray")
ref.penup()
ref.goto(x1, y1)
ref.pendown()
ref.goto(x2, y2)

# DDA Algorithm
dx = x2 - x1
dy = y2 - y1

steps = max(abs(dx), abs(dy))
x_inc = dx / steps
y_inc = dy / steps

x = x1
y = y1

for i in range(steps + 1):
    t.goto(round(x), round(y))
    t.dot(6, "blue")
    turtle.update()
    time.sleep(0.02)

    x += x_inc
    y += y_inc

turtle.done()