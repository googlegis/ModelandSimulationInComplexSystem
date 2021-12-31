from sympy import *

def fun():
    x = Symbol('x')
    y = Symbol('y')
    z = Symbol('z')
    f1 = 2 *x -y +z -10
    f2 = 3*x + 2*y -z -16
    f3 = x + 6 * y -z -28
    print(solve([f1,f2,f3]))