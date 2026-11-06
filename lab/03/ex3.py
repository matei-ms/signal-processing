import numpy as np
import matplotlib.pyplot as plt
import math

fig, axs = plt.subplots(1, 2)
fig.suptitle('Exercițiul 3')

fs = 1000

t = np.arange(0, 1, 1 / fs)
x = np.sin(2 * np.pi * 5 * t) - 2 * np.sin(2 * np.pi * 15 * t) + 1.5 * np.sin(2 * np.pi * 25 * t)

N = fs

unu = np.arange(N).reshape(N, 1)
doi = np.arange(N)

F = math.e ** (-2j * np.pi * unu * doi / N)

X = F @ x

axs[0].set_xlabel('Timp (s)')
axs[0].set_ylabel('x(t)')
axs[0].plot(t, x, color='orangered')

axs[1].set_xlabel('Frecventa (Hz)')
axs[1].set_ylabel(r'$|X(\omega)|$')
markerline, stemlines, baseline = axs[1].stem(np.arange(51), np.abs(X[:51]), linefmt='salmon', markerfmt='salmon', basefmt=' ')

plt.tight_layout()
plt.savefig('lab/03/ex3.pdf')
plt.show()