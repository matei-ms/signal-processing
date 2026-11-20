import numpy as np
import matplotlib.pyplot as plt

fig, axs = plt.subplots(4)
fig.suptitle('Exercițiul 3')

fsd = 1000

t = np.arange(0, 1, 1 / fsd)

x = np.sin(2 * np.pi * 8 * t)
y = np.sin(2 * np.pi * 28 * t)
z = np.sin(2 * np.pi * 58 * t)

fs = 125 # 2 * 58 = 116; 125 > 116

te = t[::fsd // fs]
xe = x[::fsd // fs]
ye = y[::fsd // fs]
ze = z[::fsd // fs]

axs[0].plot(t, x, color='mediumvioletred', label='8 Hz')

axs[1].plot(t, x, color='mediumvioletred')
axs[1].plot(te, xe, 'o', color='deeppink')

axs[2].plot(t, y, color='tomato', label='28 Hz')
axs[2].plot(te, ye, 'o', color='deeppink')

axs[3].plot(t, z, color='lightcoral', label='58 Hz')
axs[3].plot(te, ze, 'o', color='deeppink', label='esantioane')

for ax in axs.flat:
    ax.set_ylim([-1.1, 1.1])
    ax.grid(True)

fig.legend(loc='upper right')

plt.savefig('lab/04/ex3.pdf')
plt.show()