import sympy as sp
import numpy as np

e = np.e
def U(t):
    U=1000/(1+9*e**(-0.5*t))
    return U

x=sp.Symbol("x")
ecuacion=U(x)-800
solucion=sp.solve(ecuacion,x)

print(solucion,x)