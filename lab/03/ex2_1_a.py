import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anm
import math

fig, axs = plt.subplots(1, 2)
fig.suptitle('Figura 1')

fs = 1000
f = 2

pas = 5
fps = 25

t = np.arange(0, 1, 1 / fs)
x = np.cos(2 * np.pi * f * t)

axs[0].set_xlabel('Timp (eșantioane)')
axs[0].set_ylabel('Amplitudine')
axs[0].axhline(0, color='black', linewidth=1)
linie_x, = axs[0].plot([], [], color='green')
curent_x, = axs[0].plot([], [], 'ro')
axs[0].set_xlim([0, fs])
axs[0].set_ylim([-1.1, 1.1])

y = x * math.e ** (-2j * np.pi * t)

axs[1].set_xlabel('Real')
axs[1].set_ylabel('Imaginar')
axs[1].axhline(0, color='black', linewidth=1)
axs[1].axvline(0, color='black', linewidth=1)
linie_y, = axs[1].plot([], [], color='cornflowerblue')
curent_y, = axs[1].plot([], [], 'ro')
axs[1].set_xlim([-1.1, 1.1])
axs[1].set_ylim([-1.1, 1.1])
axs[1].set_aspect('equal')

def update(i):
    linie_x.set_xdata(np.arange(i + 1))
    linie_x.set_ydata(x[:i + 1])
    curent_x.set_xdata([i])
    curent_x.set_ydata([x[i]])

    linie_y.set_xdata(y.real[:i + 1])
    linie_y.set_ydata(y.imag[:i + 1])
    curent_y.set_xdata([y.real[i]])
    curent_y.set_ydata([y.imag[i]])

anim = anm.FuncAnimation(fig, update, frames=range(0, fs, pas), interval=1000 // fps)
anim.save('lab/03/ex2_1_a.gif', writer='pillow', fps=fps)