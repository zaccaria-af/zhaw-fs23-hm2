import numpy as np
import matplotlib.pyplot as plt


c = 1


def w(x, t):
    return np.sin(x + c * t)


def v(x, t):
    return np.sin(x + c * t) + np.cos(2 * x + 2 * c * t)


[x, t] = np.meshgrid(np.linspace(0, 10), np.linspace(0, 10))

fig = plt.figure(1)
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(x, t, w(x, t))
plt.title('Aufgabe 2b')
ax.set_xlabel('x')
ax.set_ylabel('t')
ax.set_zlabel('w')


fig = plt.figure(2)
ax = fig.add_subplot(111, projection='3d')
ax.plot_wireframe(x, t, v(x, t))
plt.title('Aufgabe 2b')
ax.set_xlabel('x')
ax.set_ylabel('t')
ax.set_zlabel('v')

plt.show()
