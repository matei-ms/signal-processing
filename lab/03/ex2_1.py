import numpy as np
import matplotlib.pyplot as plt
import math

fig, axs = plt.subplots(1, 2)
fig.suptitle('Figura 1')

fs = 1000
f = 2

t = np.arange(0, 1, 1 / fs)
x = np.cos(2 * np.pi * f * t)

axs[0].set_xlabel('Timp (eșantioane)')
axs[0].set_ylabel('Amplitudine')
axs[0].axhline(0, color='black', linewidth=1)
# axs[0].plot(x, color='green', linewidth=1)
axs[0].scatter(np.arange(fs), x, c=np.abs(x), cmap='managua', vmin=0, vmax=1, s=1)
axs[0].set_xlim([0, fs])
axs[0].set_ylim([-1.1, 1.1])

y = x * math.e ** (-2j * np.pi * t)

axs[1].set_xlabel('Real')
axs[1].set_ylabel('Imaginar')
axs[1].axhline(0, color='black', linewidth=1)
axs[1].axvline(0, color='black', linewidth=1)
# axs[1].plot(y.real, y.imag, color='cornflowerblue', linewidth=1)
axs[1].scatter(y.real, y.imag, c=np.abs(y), cmap='managua', vmin=0, vmax=1, s=1)
axs[1].set_xlim([-1.1, 1.1])
axs[1].set_ylim([-1.1, 1.1])
axs[1].set_aspect('equal')

plt.tight_layout()
plt.savefig('lab/03/ex2_1.pdf')
plt.show()