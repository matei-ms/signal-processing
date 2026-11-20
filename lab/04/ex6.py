import numpy as np
import matplotlib.pyplot as plt
import scipy.io
import math

def fft(x):
    N = len(x)
    
    if N <= 1:
        return x
    
    par = fft(x[0::2])
    impar = fft(x[1::2])
    
    xk = math.e ** (-2j * np.pi * np.arange(N // 2) / N)
    
    return np.concatenate([par + xk * impar, par - xk * impar])

fig, axs = plt.subplots()
fig.suptitle('Exercițiul 6')

# a.
fs, x = scipy.io.wavfile.read('lab/04/aeiou.wav')

N = len(x)

# b.
lg = N // 100
pas = lg // 2

col = []

doi = 2 ** int(np.ceil(np.log2(lg)))

for i in range (0, N - lg + 1, pas):
    grup = x[i:i + lg]
    grup = np.concatenate([grup, np.zeros(doi - lg)])
    
    # c.
    X = np.abs(fft(grup))
    
    # d.
    col.append(X[:doi // 2])

spectrogama = np.column_stack(col)

#e.
spectrogama = 10 * np.log10(spectrogama ** 2 + 1e-10)

axs.imshow(spectrogama, aspect='auto', origin='lower', cmap='magma', extent=[0, N / fs, 0, fs / 2 / 1000], vmin=spectrogama.max() - 80, vmax=spectrogama.max())

axs.set_xlabel('Time (s)')
axs.set_ylabel('Frequency (kHz)')
axs.set_ylim(0, 5)

plt.savefig('lab/04/ex6.pdf')
plt.show()