import matplotlib.pyplot as plt
import numpy as np


''' Aufgabe 1a) '''
''' Die maximale Weite wird bei 45 Grad erreicht (pi/2) '''
g = 9.81


def W(v0, a):
    return (v0 ** 2 * np.sin(2 * a)) / g


[v0, a] = np.meshgrid(np.linspace(0, 100), np.linspace(0, np.pi/2))

fig = plt.figure(1)
plt.title('Aufgabe 1a')
ax = fig.add_subplot(111, projection='3d')
ax.set_xlabel('v0')
ax.set_ylabel('alpha')
ax.set_zlabel('W')
surface = ax.plot_surface(v0, a, W(v0, a), cmap=plt.cm.coolwarm, linewidth = 0, antialiased = False)
fig.colorbar(surface, shrink=0.5, aspect=5)


''' Aufgabe 1b) '''
R = 8.31


def p(V, T):
    return R * T / V


def V(p, T):
    return R * T / p


def T(p, V):
    return p * V / R


[x, y] = np.meshgrid(np.linspace(0, 0.2), np.linspace(0, 1e4))
fig2 = plt.figure(2)
ax = fig2.add_subplot(111, projection='3d')
ax.plot_surface(x, y, p(x, y))
plt.title('Aufgabe 1b')
ax.set_xlabel('V')
ax.set_ylabel('T')
ax.set_zlabel('p')


[x, y] = np.meshgrid(np.linspace(1e4, 1e5), np.linspace(0, 1e4))
fig3 = plt.figure(3)
ax = fig3.add_subplot(111, projection='3d')
ax.plot_surface(x, y, V(x, y))
plt.title('Aufgabe 1b')
ax.set_xlabel('p')
ax.set_ylabel('T')
ax.set_zlabel('V')


[x, y] = np.meshgrid(np.linspace(1e4, 1e6), np.linspace(0, 10))
fig4 = plt.figure(4)
ax = fig4.add_subplot(111, projection='3d')
ax.plot_surface(x, y, T(x, y))
plt.title('Aufgabe 1b')
ax.set_xlabel('p')
ax.set_ylabel('V')
ax.set_zlabel('T')

plt.show()
