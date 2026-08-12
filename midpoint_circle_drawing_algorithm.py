import matplotlib.pyplot as plt

def midpoint_circle(xc, yc, r):
    x = 0
    y = r
    p = 1 - r

    X = []
    Y = []

    while x <= y:

        # 8 symmetric points
        points = [
            (xc + x, yc + y),
            (xc - x, yc + y),
            (xc + x, yc - y),
            (xc - x, yc - y),
            (xc + y, yc + x),
            (xc - y, yc + x),
            (xc + y, yc - x),
            (xc - y, yc - x)
        ]

        for px, py in points:
            X.append(px)
            Y.append(py)

        if p < 0:
            p += 2 * x + 3
        else:
            p += 2 * (x - y) + 5
            y -= 1

        x += 1

    return X, Y


# Input
xc, yc = map(int, input("Enter center (xc yc): ").split())
r = int(input("Enter radius: "))

# Generate circle
X, Y = midpoint_circle(xc, yc, r)

# Draw generated pixels
plt.scatter(X, Y, s=35, label="Generated Pixels")

# Draw ideal circle for comparison
theta = [i * 3.14159 / 180 for i in range(361)]

circle_x = [xc + r * __import__('math').cos(t) for t in theta]
circle_y = [yc + r * __import__('math').sin(t) for t in theta]

plt.plot(
    circle_x, circle_y,
    '--',
    color='gray',
    linewidth=1,
    label="Ideal Circle"
)

# Center
plt.scatter(xc, yc, s=60, label="Center")

plt.title("Midpoint Circle Drawing Algorithm")
plt.xlabel("X")
plt.ylabel("Y")
plt.grid(True)
plt.axis("equal")
plt.legend()
plt.show()