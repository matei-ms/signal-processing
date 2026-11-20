import numpy as np
import matplotlib.pyplot as plt
import math
import time

def dft(x):
    N = len(x)

    unu = np.arange(N).reshape(N, 1)
    doi = np.arange(N)

    F = math.e ** (-2j * np.pi * unu * doi / N)

    return F @ x

def fft(x):
    N = len(x)
    
    if N <= 1:
        return x
    
    par = fft(x[0::2])
    impar = fft(x[1::2])
    
    xk = math.e ** (-2j * np.pi * np.arange(N // 2) / N)
    
    return np.concatenate([par + xk * impar, par - xk * impar])

Ns = [128, 256, 512, 1024, 2048, 4096, 8192]

timpi = {'DFT': [], 'FFT': [], 'numpy.fft': []}

for N in Ns:
    fs = N
    t = np.arange(0, 1, 1 / fs)
    x = np.sin(2 * np.pi * 5 * t)
    
    for nume, f in [('DFT', dft), ('FFT', fft), ('numpy.fft', np.fft.fft)]:
        start = time.perf_counter()
        
        f(x)
        
        timpi[nume].append(time.perf_counter() - start)

fig, axs = plt.subplots()
fig.suptitle('Exercițiul 1')

axs.plot(Ns, timpi['DFT'], color='orangered', label='DFT')
axs.plot(Ns, timpi['FFT'], color='purple', label='FFT')
axs.plot(Ns, timpi['numpy.fft'], color='cornflowerblue', label='numpy.fft')

axs.set_xlabel('N')
axs.set_ylabel('Timp (s)')
axs.set_yscale('log')
axs.legend()
axs.grid(True)

plt.savefig('lab/04/ex1.pdf')
plt.show()