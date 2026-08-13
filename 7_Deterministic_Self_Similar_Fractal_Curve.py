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

    # Rotate the middle segment by 60 degrees
    C = (
        A[0] + dx * math.cos(math.pi/3) - dy * math.sin(math.pi/3),
        A[1] + dx * math.sin(math.pi/3) + dy * math.cos(math.pi/3)
    )

    koch(p1, A, n-1)
    koch(A, C, n-1)
    koch(C, B, n-1)
    koch(B, p2, n-1)


# Starting line
p1 = (0, 0)
p2 = (10, 0)

# Recursion level
n = 3

koch(p1, p2, n)

plt.title("Deterministic Self-Similar Fractal Curve - Koch Curve")
plt.axis("equal")
plt.axis("off")
plt.show()