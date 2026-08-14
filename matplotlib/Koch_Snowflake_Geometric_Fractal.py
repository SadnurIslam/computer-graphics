import matplotlib.pyplot as plt
import math

def koch(p1, p2, n):
    if n == 0:
        plt.plot([p1[0], p2[0]], [p1[1], p2[1]], 'k')
        return

    x1, y1 = p1
    x2, y2 = p2

    dx = (x2 - x1) / 3
    dy = (y2 - y1) / 3

    A = (x1 + dx, y1 + dy)
    B = (x1 + 2*dx, y1 + 2*dy)

    C = (
        A[0] + dx * math.cos(math.pi/3) - dy * math.sin(math.pi/3),
        A[1] + dx * math.sin(math.pi/3) + dy * math.cos(math.pi/3)
    )

    koch(p1, A, n-1)
    koch(A, C, n-1)
    koch(C, B, n-1)
    koch(B, p2, n-1)


# Equilateral triangle
P1 = (0, 0)
P2 = (10, 0)
P3 = (5, 5 * math.sqrt(3))

n = 3

koch(P1, P2, n)
koch(P2, P3, n)
koch(P3, P1, n)

plt.title("Koch Snowflake")
plt.axis("equal")
plt.axis("off")
plt.show()