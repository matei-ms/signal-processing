import numpy as np
import matplotlib.pyplot as plt

fig, axs = plt.subplots(3)
fig.suptitle('Exercițiul 4')

t = np.linspace(0, 0.03, 1600)
s1 = np.sin(2 * np.pi * 400 * t)
s2 = 3 * (2 * (t * 200 - np.floor(t * 200)) - 1)

axs[0].plot(t, s1, color='red', label='sin')
axs[1].plot(t, s2, color='green', label='saw')
axs[2].plot(t, s1 + s2, color='gray', label='sum')

for ax in axs.flat:
    ax.grid(True)

fig.legend(loc='upper right')

plt.savefig('lab/02/ex4.pdf')
plt.show()