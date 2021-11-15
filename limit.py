import sympy as sp
x=sp.Symbol('x') # 
f=8-3*x+12*x**2 # Expression
L=sp.limit(f,x,2) # Limit function
print("The Limit is:",L)