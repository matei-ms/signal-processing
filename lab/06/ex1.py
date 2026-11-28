import numpy as np
import matplotlib.pyplot as plt

fig, axs = plt.subplots(2, 2)
fig.suptitle('Exercițiul 1')

B = 1
# pentru ca functia reconstruita sa arate corect fs >= 2B
# pentru B < 0.5 toate graficele arata corect

t = np.linspace(-3, 3, 1000)
x = np.sinc(B * t) ** 2 # sinc(x) = sin(pix) / pix

fss = [1, 1.5, 2, 4]

for ax, fs in zip(axs.flat, fss):
    Ts = 1 / fs

    te = np.arange(-np.floor(3 / Ts), np.floor(3 / Ts) + 1) * Ts
    
    xe = np.sinc(B * te) ** 2
    sincs = np.sinc((t.reshape(len(t), 1) - te) / Ts)
    
    xr = sincs @ xe

    ax.plot(t, x, color='black')
    ax.plot(t, xr, '--', color='limegreen')
    ax.stem(te, xe, linefmt='darkorange', markerfmt='o', basefmt=' ')

    ax.set_title(f'fs = {fs}Hz')
    ax.set_xlabel('t[s]')
    ax.set_ylabel('Amplitudine')
    ax.grid(True)

plt.tight_layout()
plt.savefig('lab/06/ex1.pdf')
plt.show()