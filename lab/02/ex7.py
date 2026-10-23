import numpy as np
import matplotlib.pyplot as plt

fig, axs = plt.subplots(3)
fig.suptitle('Exercițiul 7')

fs = 1000

t = np.arange(0, 1, 1 / fs)
s = np.sin(2 * np.pi * 30 * t)

axs[0].plot(t, s, color='red')

ta = t[::4]
sa = s[::4]

axs[1].plot(ta, sa, color='deeppink')

# a. arata aproape la fel; e doar putin stramb

tb = t[1::4]
sb = s[1::4]

axs[2].plot(tb, sb, color='deeppink')

# b. aseamana; arata ca o diferenta de faza mica

for ax in axs.flat:
    ax.grid(True)

plt.savefig('lab/02/ex7.pdf')
plt.show()