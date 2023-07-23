# -*- coding: utf-8 -*-
"""
Created on Mon Jul  3 08:40:00 2023

@author: 34626
"""

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation 


R = 0.04
x= 0.1
m = 1.360+0.3
g = 9.81
L = 0.95
e = 0.001
Ix = (1/2*R**2+ L**2)*m
Iy = (1/2*R**2 + x**2 + (L+e)**2)*m
wx = np.sqrt(m*g*L/Ix)
wy = np.sqrt(m*g*L/Iy)
Tx, Ty = 2*np.pi/wx, 2*np.pi/wy

print(Tx, Ty)
t = np.linspace(0, 60, 2400)


wx = np.pi
wy = wx/np.sqrt(2)


T = t
x = np.sin(wx*T)
y = np.sin(wy*T)


fig = plt.figure()
ax = fig.add_subplot(111, xlim=(-1.2, 1.2), ylim=(-1.2, 1.2))
plt.axis('off')


pendulum, = ax.plot([],[], 'o')
trajectory, = ax.plot([],[], '-', lw = 0.5, alpha = 0.75)
def init():
    trajectory.set_data([], [])
    pendulum.set_data([],[])
    
    return pendulum, trajectory
def animate(i):
    trajectory.set_data([x[:i]], [y[:i]])
    pendulum.set_data([x[i]], [y[i]])
    
    return pendulum, trajectory

fig.patch.set_facecolor('black') 
ani = animation.FuncAnimation(fig, animate, np.arange(len(t)), blit = True, init_func = init)
dpi = 200
writer = animation.writers['ffmpeg'](fps=30)
ani.save('lissajous1_s2.mp4',writer=writer,dpi=dpi)
