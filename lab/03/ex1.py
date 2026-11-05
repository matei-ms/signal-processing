import numpy as np
import matplotlib.pyplot as plt
import math

N = 8

unu = np.arange(N).reshape(N, 1)
doi = np.arange(N)

F = math.e ** (-2j * np.pi * unu * doi / N)

fig, axs = plt.subplots(N)
fig.suptitle('Exercițiul 1')

for i in range(N):
    axs[i].plot(F[i].real, color='orange')
    axs[i].plot(F[i].imag, color='limegreen')

# verificare:
print(np.allclose(F.conj().T @ F, N * np.eye(N)))

plt.savefig('lab/03/ex1.pdf')
plt.show()