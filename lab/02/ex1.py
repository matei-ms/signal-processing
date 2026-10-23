import numpy as np
import matplotlib.pyplot as plt

fig, axs = plt.subplots(2)
fig.suptitle('Exercițiul 1')

t = np.linspace(0, 0.03, 1600)
s = 1.1 * np.sin(2 * np.pi * 420 * t + 0.1)

axs[0].plot(t, s, color='dodgerblue', label='sin')

s = 1.1 * np.cos(2 * np.pi * 420 * t + 0.1 - np.pi / 2)

axs[1].plot(t, s, color='crimson', label='cos')

for ax in axs.flat:
    ax.grid(True)

fig.legend(loc='upper right')

plt.savefig('lab/02/ex1.pdf')
plt.show()