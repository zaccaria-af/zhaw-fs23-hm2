import sympy as sym
import numpy as np

def nrm(a): return np.linalg.norm(a, 2)

def dampened_newton(f, Df, x0, tol=1e-5, kmax: int = 4):
    xn = np.copy(x0)
    while nrm(f(xn)) > tol:
        print(f'{xn=}')
        fxn = f(xn)
        print(f'||f(xn)||_2 = {nrm(fxn)}')
        dn = np.linalg.solve(Df(xn), -fxn)
        print(f'||xn - x(n-1)||_2 = {nrm(dn)}')

        base_nrm = nrm(fxn)
        min_k = 0
        for k in range(1, kmax + 1):
            if nrm(f(xn + dn / 2**k)) < base_nrm:
                min_k = k
                break

        xn = xn + dn / 2**min_k

x, y, z = sym.symbols('x, y, z')


sf1 = x + y**2 - z**3 - 13
sf2 = sym.log(y/4) + sym.exp(0.5 * z - 1) - 1 # type: ignore
sf3 = (y - 3)**2 - z**3 + 7

sf = sym.Matrix([sf1, sf2, sf3])
sDf = sf.jacobian([x, y, z])

f = sym.lambdify([([x], [y], [z])], sf)
Df = sym.lambdify([([x], [y], [z])], sDf)

x0 = np.array([[1.5], [3], [2.5]])

dampened_newton(f, Df, x0)