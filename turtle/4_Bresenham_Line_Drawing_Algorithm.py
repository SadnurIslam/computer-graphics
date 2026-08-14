import turtle
import time

# ---------------- Screen ----------------
turtle.setup(700, 700)
turtle.bgcolor("white")
turtle.title("Bresenham Line Drawing Algorithm")
turtle.tracer(0)

# ---------------- Axes ----------------
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

axis.penup()
axis.goto(285, -15)
axis.write("X")
axis.goto(10, 285)
axis.write("Y")

# ---------------- Drawing Turtle ----------------
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.penup()

# ---------------- Input ----------------
x1 = int(input("Enter x1: "))
y1 = int(input("Enter y1: "))
x2 = int(input("Enter x2: "))
y2 = int(input("Enter y2: "))

# Reference (ideal) line
ref = turtle.Turtle()
ref.hideturtle()
ref.speed(0)
ref.color("lightgray")
ref.penup()
ref.goto(x1, y1)
ref.pendown()
ref.goto(x2, y2)

# ---------------- Bresenham Algorithm ----------------
dx = abs(x2 - x1)
dy = abs(y2 - y1)

sx = 1 if x1 < x2 else -1
sy = 1 if y1 < y2 else -1

x, y = x1, y1

if dx >= dy:
    p = 2 * dy - dx

    while True:
        t.goto(x, y)
        t.dot(6, "blue")
        turtle.update()
        time.sleep(0.02)

        if x == x2:
            break

        x += sx

        if p < 0:
            p += 2 * dy
        else:
            y += sy
            p += 2 * (dy - dx)

else:
    p = 2 * dx - dy

    while True:
        t.goto(x, y)
        t.dot(6, "blue")
        turtle.update()
        time.sleep(0.02)

        if y == y2:
            break

        y += sy

        if p < 0:
            p += 2 * dx
        else:
            x += sx
            p += 2 * (dx - dy)

turtle.done()