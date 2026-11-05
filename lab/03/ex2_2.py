import numpy as np
import matplotlib.pyplot as plt
import math

fig, axs = plt.subplots(2, 2)
fig.suptitle('Figura 2')

fs = 1000
f = 2

t = np.arange(0, 1, 1 / fs)
x = np.cos(2 * np.pi * f * t)

omegas = [1, 2, 5, 7]

for ax, w in zip(axs.flat, omegas):
    ax.set_xlabel('Real')
    ax.set_ylabel('Imaginar')
    ax.axhline(0, color='black', linewidth=1)
    ax.axvline(0, color='black', linewidth=1)
    ax.set_xlim([-1.1, 1.1])
    ax.set_ylim([-1.1, 1.1])
    ax.set_aspect('equal')
    
    z = x * math.e ** (-2j * np.pi * w * t)
    
    ax.scatter(z.real, z.imag, c=np.abs(z), cmap='managua', vmin=0, vmax=1, s=1)

plt.savefig('lab/03/ex2_2.pdf')
plt.show()