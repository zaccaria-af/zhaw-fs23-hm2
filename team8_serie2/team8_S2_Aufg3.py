import sympy as sp

''' Aufgabe 3: Linearisieren der Funktion f '''
x, y, z = sp.symbols('x y z')
f1 = x + y**2 - z**2 - 13
f2 = sp.ln(y/4) + sp.exp(0.5 * z - 1) - 1
f3 = (y - 3)**2 - z**3 + 7

x0 = sp.Matrix([1.5, 3, 2.5]).T
f = sp.Matrix([f1, f2, f3])
X = sp.Matrix([x, y, z])
Df = f.jacobian(X)
print(f'Jacobi-Matrix: {Df}')

# Linearisierung
f0 = f.subs([(x, x0[0]), (y, x0[1]), (z, x0[2])])
f0 = f0.evalf()
Df0 = Df.subs([(x, x0[0]), (y, x0[1]), (z, x0[2])])
Df0 = Df0.evalf()

p1 = x - x0[0]
p2 = y - x0[1]
p3 = z - x0[2]
p = sp.Matrix([p1, p2, p3])

g = f0 + Df0 * p
g = g.evalf()
print(f'g: {g}')