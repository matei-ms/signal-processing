import numpy as np
import matplotlib.pyplot as plt

fig, axs = plt.subplots(4)
fig.suptitle('Semnale sinusoidale')

t = np.linspace(0, 0.03, 1600)
s = np.sin(2 * np.pi * 400 * t)

axs[0].plot(t, s, color='red', label='a.')

t = np.linspace(0, 3, 10000)
s = np.sin(2 * np.pi * 800 * t)
    
axs[1].plot(t, s, color='orange', label='b.')

t = np.linspace(0, 0.03, 1600)
s = 2 * (t * 240 - np.floor(t * 240)) - 1

axs[2].plot(t, s, color='green', label='c.')

t = np.linspace(0, 0.03, 1600)
s = np.sign(np.sin(2 * np.pi * 300 * t))

axs[3].plot(t, s, color='blue', label='d.')

for ax in axs.flat:
    ax.set_ylim([-1.1, 1.1])
    ax.grid(True)

fig.legend(loc='upper right')

plt.savefig('lab/01/ex2.pdf')
plt.show()