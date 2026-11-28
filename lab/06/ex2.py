import numpy as np
import matplotlib.pyplot as plt

fig, axs = plt.subplots(4, 2)
fig.suptitle('Exercițiul 2')

N = 100

x = np.random.rand(N)

y = np.zeros(N)
y[35:65] = 1

for i in range(4):
    axs[i, 0].plot(x, color='rebeccapurple')
    axs[i, 1].plot(y, color='mediumpurple')

    x = np.convolve(x, x)
    y = np.convolve(y, y)

axs[0, 0].set_title('Aleator')
axs[0, 1].set_title('Bloc rectangular')

for ax in axs.flat:
    ax.grid(True)
    
plt.tight_layout()
plt.savefig('lab/06/ex2.pdf')
plt.show()

# ambele arata din ce in ce mai mult a distributie normala
# semnalului aleator ii dispare din zgomot dupa fiecare convolutie