import numpy as np
import math
from matplotlib import pyplot as plt

t = np.arange(0, 3.001, 0.001) #tiempo
posy = []
posv = []
v=0
yi=1
g=9.80665
tc=0
for i in range (0,len(t)):
    y=-(0.5*g*((t[i]-tc)**2))+yi+v*(t[i]-tc)
    if y<=0:
        v=-(v-g*(t[i]-tc))*0.75
        yi=0
        tc=t[i]
        print(v,t[i],tc)
    posy.append(y)
    posv.append(v)#dummy function
#with plt.xkcd():
while(True):
    plt.figure(1)
    plt.plot(t,posy, label='Posición y(t)')
    plt.title("Posición y(t)")
    plt.xlabel("tiempo (s)")
    plt.ylabel("altura (m)")
    plt.legend()
    plt.grid()
    plt.show()
    break
while(True):
    plt.figure(2)
    plt.plot(t,posv, label='Posición y(t)')
    plt.title("Posición y(t)")
    plt.xlabel("tiempo (s)")
    plt.ylabel("altura (m)")
    plt.legend()
    plt.grid()
    plt.show()
    break