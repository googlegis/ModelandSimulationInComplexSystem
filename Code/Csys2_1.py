import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def diff_equation(y,x):
    return np.array(y)
def fun():
    x=np.linspace(0,1,num=100)
    result=odeint(diff_equation,1,x)
    plt.plot(x,result[:,0])
    plt.grid()
    plt.show()