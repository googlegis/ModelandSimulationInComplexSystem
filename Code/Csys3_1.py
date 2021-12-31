# 初级元胞自动机

import numpy as np
import matplotlib.pyplot as plt

def gen_next(s,no):
    n = bin(no)
    n=n[2:].zfill(8)
    nl=len(s)
    k=s[(nl-1):]+s+s[0:1]
    r=[]
    for i in range(1,nl+1):
        t=eval('0b' + ''.join(map(str,k[i-1:i+2])))
        r.append(n[7-t])
    return list(map(eval,r))

def fun():
    ar=np.ndarray(shape=(300,300),dtype="bool")
    no=90
    row=np.ndarray(shape=ar.shape[1],dtype="int")
    row[:]=0
    row[len(row)//2]=1
    for i in range(ar.shape[0]):
        ar[i,:]=row
        row=gen_next(row,no)
    plt.figure(1)
    plt.imshow(ar)
    plt.show()


