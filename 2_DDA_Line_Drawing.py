import matplotlib.pyplot as plt

x1, y1 = map(int, input("Enter x1 y1: ").split())
x2, y2 = map(int, input("Enter x2 y2: ").split())

dx = x2 - x1
dy = y2 - y1

steps = max(abs(dx), abs(dy))

x_inc = dx / steps
y_inc = dy / steps

x = x1
y = y1

X = []
Y = []

for i in range(steps + 1):
    X.append(round(x))
    Y.append(round(y))

    x += x_inc
    y += y_inc

# DDA generated pixels
plt.scatter(X, Y, s=40)

# Ideal line between endpoints
plt.plot([x1, x2], [y1, y2],
         linestyle='--', color='gray', linewidth=0.8)

plt.plot(X, Y, linestyle='-', color='blue', linewidth=1, label='DDA Pixels')

plt.xlabel("X")
plt.ylabel("Y")
plt.title("DDA Line Drawing Algorithm")
plt.grid(True)
plt.axis("equal")
plt.show()