import sympy as sp
x=sp.Symbol('x')
f=sp.sin(x)+x**2+sp.exp(4*x)
print(f)
df=sp.diff(f,x)
print(df)