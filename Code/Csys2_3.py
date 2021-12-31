# Matplotlib 显示三维图形实例
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

def fun():
    fig = plt.figure()
    ax = Axes3D(fig)
    x = np.linspace(-1,1,50)
    y = np.linspace(-1,1,50)
    xs,ys = np.meshgrid(x,y)
    zs = xs**2 - ys**2
    ax.plot_surface(xs,ys,zs)
    plt.show()