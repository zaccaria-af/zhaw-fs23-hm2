import sympy as sp
sp.init_printing(pretty_print=True)

''' Aufgabe 2: Jacobi-Matrix a) '''
x, y = sp.symbols('x y')
f1 = 5*x*y
f2 = x**2 * y**2 + x + 2*y

f = sp.Matrix([f1, f2])
X = sp.Matrix([x, y])
Df = f.jacobian(X)
sp.pprint(f'Jacobi-Matrix a: {Df}')

''' Aufgabe 2: Jacobi-Matrix b) '''
x, y, z = sp.symbols('x y z')
f1 = sp.ln(x**2 + y**2) + z**2
f2 = sp.exp(y**2 + z**2) + x**2
f3 = 1 / (z**2 + x**2) + y**2

f = sp.Matrix([f1, f2, f3])
X = sp.Matrix([x, y, z])
Df = f.jacobian(X)
print(f'Jacobi-Matrix b: {Df}')