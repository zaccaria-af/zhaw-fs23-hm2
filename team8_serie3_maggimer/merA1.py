import sympy as sym
import numpy as np

x, y = sym.symbols('x, y')

sf1 = 20 - 18*x - 2*y**2
sf2 = -4*y * (x -y**2)


sf = sym.Matrix([sf1, sf2])

sDf = sf.jacobian([x, y])

f = sym.lambdify([([x], [y])], sf)
Df = sym.lambdify([([x], [y])], sDf)

x0 = np.array([[1.1], [0.9]])

xk = x0.copy()

for k in range(2):
    print(f'x{k} = {xk}')
    fxk = f(xk)
    print(f'||f(xk)||_2 = {np.linalg.norm(fxk, 2)}')
    dk = np.linalg.solve(Df(xk), -fxk)
    print(f'||xk - x(k-1)||_2 = {np.linalg.norm(dk, 2)}')
    xk = xk + dk


