import turtle
import time

# ---------- Screen ----------
screen = turtle.Screen()
screen.setup(700, 700)
screen.title("2D Translation")

turtle.tracer(0)

# ---------- Axes ----------
axis = turtle.Turtle()
axis.hideturtle()
axis.speed(0)
axis.color("gray")


# # X-axis
axis.penup()
axis.goto(-300, 0)
axis.pendown()
axis.goto(300, 0)

# # Y-axis
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

# Translation vector
# tx = int(input("Enter tx: "))
# ty = int(input("Enter ty: "))

tx = 30
ty = 20

# Draw polygon
def draw(poly, color):
    t.penup()
    t.goto(poly[0])
    t.pendown()
    t.color(color)

    for p in poly[1:]:
        t.goto(p)

    t.goto(poly[0])


# ---------- Animation ----------
steps = 50

for i in range(steps + 1):
    t.clear()

    # Original object
    draw(triangle, "gray")

    # Current translated position
    dx = tx * i / steps
    dy = ty * i / steps

    moved = [(x + dx, y + dy) for x, y in triangle]

    # Moving object
    draw(moved, "blue")

    turtle.update()
    time.sleep(0.03)

turtle.done()