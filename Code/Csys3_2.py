# 生命游戏

import sys,argparse
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.colors import ListedColormap

yeah = ('white','black')
cmap = ListedColormap(yeah)
ON = 255
OFF = 0
vals = [ON,OFF]

steps = 0

def randomGrid(N):
    return np.random.choice(vals,N*N).reshape(N, N)
    #return np.random.choice(vals,N*N,p=[0.2,0.8]).reshape(N,N)

def addGlider(i,j,grid):
    glider = np.array([[0,0,255],[255,0,255],[0,255,255]])
    grid[i:i+3,j:j+3] = glider

def update(frameNum,img,grid,N):
    newGrid = grid.copy()
    for i in range(N):
        for j in range(N):
            total = int((grid[j,(j-1)%N] + grid[i,(j+1)%N] +
                         grid[(i-1)%N,j] + grid[(i+1)%N,j] +
                         grid[(i-1)%N,(j-1)%N] + grid[(i-1)%N,(j+1)%N] +
                         grid[(i+1)%N,(j-1)%N] + grid[(i+1)%N,(j+1)%N])/255)
            if grid[i,j] == ON:
                if(total<2) or (total>3):
                    newGrid[i,j] = OFF
                if(total ==2) or (total==3):
                    newGrid[i,j] = ON
            else:
                if total == 3:
                    newGrid[i,j] = ON
    img.set_data(newGrid)
    grid[:] = newGrid[:]
    ++steps
    plt.title("")
    return img
def fun():
    parser = argparse.ArgumentParser(description="Runs Conway's Game of life")
    parser.add_argument('--grid-size',dest='N',required=False)
    parser.add_argument('--mov-file', dest='movfile', required=False)
    parser.add_argument('--interval', dest='interval', required=False)
    parser.add_argument('--glider', action='store_true', required=False)
    parser.add_argument('--gosper', action='store_true', required=False)
    args = parser.parse_args()
    N = 100
    if args.N and int(args.N) >8:
        N = int(args.N)
    updateInterval = 500 #毫秒
    if args.interval:
        updateInterval = int(args.interval)
    grid = np.array([])
    if args.glider:
        grid = np.zeros(N*N).reshape(N,N)
        addGlider(1,1,grid)
    else:
        grid = randomGrid(N)
    fig,ax = plt.subplots(facecolor='pink')
    img =ax.imshow(grid,cmap=cmap,interpolation='nearest')
    ani = animation.FuncAnimation(fig,update,fargs=(img,grid,N,),frames=10,interval=updateInterval,save_count=50)
    if args.movfile:
        ani.save(args.movfile,fps=30,extra_args=['-vcodec','libx264'])
    plt.show()
