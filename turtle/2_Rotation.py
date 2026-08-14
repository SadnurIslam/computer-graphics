import turtle
import math
import time

# ---------- Screen ----------
screen = turtle.Screen()
screen.setup(700, 700)
screen.title("2D Rotation")
turtle.tracer(0)

# ---------- Axes ----------
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

# ---------- Drawing Turtle ----------
t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pensize(2)

# Original triangle
triangle = [(50, 50), (150, 50), (100, 150)]

# Rotation angle
angle = int(input("Enter rotation angle: "))

# Draw polygon
def draw(poly, color):
    t.penup()
    t.goto(poly[0])
    t.pendown()
    t.color(color)

    for p in poly[1:]:
        t.goto(p)

    t.goto(poly[0])

# Rotate polygon
def rotate(poly, theta):
    new = []
    r = math.radians(theta)

    for x, y in poly:
        xr = x * math.cos(r) - y * math.sin(r)
        yr = x * math.sin(r) + y * math.cos(r)
        new.append((xr, yr))

    return new

# ---------- Animation ----------
steps = 60

for i in range(steps + 1):
    t.clear()

    # Original object
    draw(triangle, "gray")

    # Current angle
    current = angle * i / steps

    # Rotated object
    rotated = rotate(triangle, current)
    draw(rotated, "blue")

    # Rotation point
    t.penup()
    t.goto(0, 0)
    t.dot(8, "red")

    turtle.update()
    time.sleep(0.03)

turtle.done()