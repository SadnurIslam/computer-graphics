import turtle
import time

# Screen
screen = turtle.Screen()
screen.setup(600, 600)
screen.title("Koch Snowflake")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pensize(2)

# Koch function
def koch(length, n):
    if n == 0:
        t.forward(length)
        return

    length /= 3
    koch(length, n-1)
    t.left(60)
    koch(length, n-1)
    t.right(120)
    koch(length, n-1)
    t.left(60)
    koch(length, n-1)

# Draw one snowflake level
def draw_level(level):
    t.clear()

    t.penup()
    t.goto(-150, 90)
    t.setheading(0)
    t.pendown()

    for _ in range(3):
        koch(300, level)
        t.right(120)

    t.penup()
    t.goto(-250, 250)
    t.write(f"Level = {level}", font=("Arial", 14, "bold"))

# Maximum complexity
k = 4

# Show all levels
for level in range(k + 1):
    draw_level(level)
    time.sleep(2)

turtle.done()