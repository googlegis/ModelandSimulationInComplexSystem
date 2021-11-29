import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

def diff_equation(y_list,x):
    y,z=y_list
    return np.array([z,-y])

def Fun():
    x=np.linspace(0,np.pi*2,num=100)
    y0=[1,1] #y(0)=1,y'(0)=1
    result=odeint(diff_equation,y0,x)
    plt.plot(x,result[:,0],label='y')#y的图像，y=cos(x)+sin(x)
    plt.plot(x,result[:,1],label='z')#z的图像，也就是y'的图像，z=-sin(x)+cos(x)
    plt.legend()
    plt.grid()
    plt.show()