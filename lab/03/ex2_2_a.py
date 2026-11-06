import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as anm
import math

fig, axs = plt.subplots(2, 2)
fig.suptitle('Figura 2')

fs = 1000
f = 2

pas = 5
fps = 25

t = np.arange(0, 1, 1 / fs)
x = np.cos(2 * np.pi * f * t)

omegas = [1, 2, 5, 7]

for ax, w in zip(axs.flat, omegas):
    ax.set_title(rf'$\omega = {w}$', x=0.8, y=1)
    ax.set_xlabel('Real')
    ax.set_ylabel('Imaginar')
    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)
    ax.set_xlim([-1.1, 1.1])
    ax.set_ylim([-1.1, 1.1])
    ax.set_aspect('equal')

z1 = x * math.e ** (-2j * np.pi * omegas[0] * t)
z2 = x * math.e ** (-2j * np.pi * omegas[1] * t)
z3 = x * math.e ** (-2j * np.pi * omegas[2] * t)
z4 = x * math.e ** (-2j * np.pi * omegas[3] * t)

linie_1, = axs[0, 0].plot([], [], color='cornflowerblue')
curent_1, = axs[0, 0].plot([], [], 'ro')
linie_2, = axs[0, 1].plot([], [], color='cornflowerblue')
curent_2, = axs[0, 1].plot([], [], 'ro')
linie_3, = axs[1, 0].plot([], [], color='cornflowerblue')
curent_3, = axs[1, 0].plot([], [], 'ro')
linie_4, = axs[1, 1].plot([], [], color='cornflowerblue')
curent_4, = axs[1, 1].plot([], [], 'ro')

def update(i):
    linie_1.set_xdata(z1.real[:i + 1])
    linie_1.set_ydata(z1.imag[:i + 1])
    curent_1.set_xdata([z1.real[i]])
    curent_1.set_ydata([z1.imag[i]])

    linie_2.set_xdata(z2.real[:i + 1])
    linie_2.set_ydata(z2.imag[:i + 1])
    curent_2.set_xdata([z2.real[i]])
    curent_2.set_ydata([z2.imag[i]])

    linie_3.set_xdata(z3.real[:i + 1])
    linie_3.set_ydata(z3.imag[:i + 1])
    curent_3.set_xdata([z3.real[i]])
    curent_3.set_ydata([z3.imag[i]])

    linie_4.set_xdata(z4.real[:i + 1])
    linie_4.set_ydata(z4.imag[:i + 1])
    curent_4.set_xdata([z4.real[i]])
    curent_4.set_ydata([z4.imag[i]])

anim = anm.FuncAnimation(fig, update, frames=range(0, fs, pas), interval=1000 // fps)
anim.save('lab/03/ex2_2_a.gif', writer='pillow', fps=fps)

plt.savefig('lab/03/ex2_2.pdf')
plt.show()