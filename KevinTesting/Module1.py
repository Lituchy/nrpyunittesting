import sympy as sp

def Module1(boo):
    global x,y,z
    x,y,z,a,b = sp.symbols('x y z a b')
    if boo:
        x = a**2
        y = b**2
        z = 2*a*b
    else:
        x = a/b
        y = a**2-b**2
        z = a*b+1