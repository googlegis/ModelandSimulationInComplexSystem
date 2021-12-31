import sympy as sy
def differential_equation(x,f):
    return sy.diff(f(x),x,2) + f(x) #f(x)''+f(x)=0 二阶常系数齐次微分方程

def fun():
    x = sy.symbols('x')
    y= sy.Function('f')
    print(sy.dsolve(differential_equation(x,f),f(x)))
    sy.pprint(sy.dsolve(differential_equation(x,f),f(x)))
