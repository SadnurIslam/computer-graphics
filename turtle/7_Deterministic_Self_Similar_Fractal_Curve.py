import turtle
import time

# -------- Screen --------
screen = turtle.Screen()
screen.setup(800, 400)
screen.title("Koch Curve - Complexity 0 to k")

t = turtle.Turtle()
t.hideturtle()
t.speed(0)
t.pensize(2)

# -------- Koch Function --------
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

# -------- Draw One Level --------
def draw_level(level):
    t.clear()

    t.penup()
    t.goto(-300, 0)
    t.setheading(0)
    t.pendown()

    koch(600, level)

    t.penup()
    t.goto(-380, 160)
    t.write(f"Complexity Level = {level}",
            font=("Arial", 14, "bold"))

# -------- Input --------
k = int(input("Enter maximum complexity: "))

# -------- Show All Levels --------
for level in range(k + 1):
    draw_level(level)
    time.sleep(2)

turtle.done()