import numpy as np
import matplotlib.pyplot as plt

fig, axs = plt.subplots(3)
fig.suptitle('Exercițiul 1')

# [0 : 0.0005 : 0.03]
t = np.linspace(0, 0.03, round(0.03/0.0005) + 1)

x = np.cos(520 * np.pi * t + np.pi / 3)
y = np.cos(280 * np.pi * t - np.pi / 3)
z = np.cos(120 * np.pi * t + np.pi / 3)

axs[0].plot(t, x, color='salmon', label='x(t)')
axs[1].plot(t, y, color='orangered', label='y(t)')
axs[2].plot(t, z, color='indianred', label='z(t)')

for ax in axs.flat:
    ax.set_ylim([-1.1, 1.1])
    ax.grid(True)
    
fig.legend(loc='upper right')

plt.savefig('lab/01/ex1.pdf')
plt.show()