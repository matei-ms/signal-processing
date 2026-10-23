import numpy as np
import matplotlib.pyplot as plt

fig, axs = plt.subplots(3)
fig.suptitle('Exercițiul 8')

a = np.linspace(-np.pi / 2, np.pi / 2, 1000)

sina = np.sin(a)
pade = (a - 7 * a ** 3 / 60) / (1 + a * a / 20)

axs[0].plot(a, sina, color='green', label='sin')
axs[0].plot(a, a, color='purple', label='taylor')
axs[0].plot(a, pade, color='pink', label='pade')
axs[0].legend()

axs[1].plot(a, np.abs(a - sina), color='purple', label='eroare taylor')
axs[1].plot(a, np.abs(pade - sina), color='pink', label='eroare pade')
axs[1].legend()

axs[2].plot(a, np.abs(a - sina), color='purple', label='eroare taylor')
axs[2].plot(a, np.abs(pade - sina), color='pink', label='eroare pade')
axs[2].set_yscale('log')
axs[2].legend()

for ax in axs.flat:
    ax.grid(True)

plt.savefig('lab/02/ex8.pdf')
plt.show()