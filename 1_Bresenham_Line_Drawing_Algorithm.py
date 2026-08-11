import matplotlib.pyplot as plt

x1, y1 = map(int, input("Enter x1 y1: ").split())
x2, y2 = map(int, input("Enter x2 y2: ").split())

dx = abs(x2 - x1)
dy = abs(y2 - y1)

sx = 1 if x1 < x2 else -1
sy = 1 if y1 < y2 else -1

x, y = x1, y1

X = []
Y = []

if dx > dy:
    p = 2 * dy - dx

    while True:
        X.append(x)
        Y.append(y)

        if x == x2:
            break

        x += sx

        if p < 0:
            p += 2 * dy
        else:
            y += sy
            p += 2 * dy - 2 * dx

else:
    p = 2 * dx - dy

    while True:
        X.append(x)
        Y.append(y)

        if y == y2:
            break

        y += sy

        if p < 0:
            p += 2 * dx
        else:
            x += sx
            p += 2 * dx - 2 * dy

# Draw the Bresenham pixels
plt.scatter(X, Y, s=50, color='blue', label='Bresenham Pixels')

# Direct line connecting the two endpoints
plt.plot([x1, x2], [y1, y2], linewidth=1, label='Direct Line')

# Connect pixels so the line is clearly visible
plt.plot(X, Y, linestyle='--', color='gray', linewidth=0.5)



plt.xlabel("X")
plt.ylabel("Y")
plt.title("Bresenham Line Drawing Algorithm")
plt.grid(True)
plt.axis("equal")
plt.show()