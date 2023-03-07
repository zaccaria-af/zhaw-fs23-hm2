import sympy as sym
import numpy as np

x, y = sym.symbols('x, y')

print('Aufgabe a)')

f1 = x ** 2/186**2 - y ** 2/(300**2 - 186**2) - 1
f2 = (y - 500)**2/279**2 - (x - 300)**2/(500**2 - 279**2) - 1
p1 = sym.plot_implicit(sym.Eq(f1, 0), (x, -2000, 2000), (y, -2000, 2000))
p2 = sym.plot_implicit(sym.Eq(f2, 0), (x, -2000, 2000), (y, -2000, 2000))
p1.append(p2[0])
p1.show()

print('Aufgabe b)')
