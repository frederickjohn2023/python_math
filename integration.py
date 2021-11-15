from sympy import *
x = symbols('x')
exp = x**2 + 4*x + 12
i = integrate(exp,x)
print(i)