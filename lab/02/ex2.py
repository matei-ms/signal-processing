import numpy as np
import matplotlib.pyplot as plt

fig, axs = plt.subplots(2)
fig.suptitle('Exercițiul 2')

t = np.linspace(0, 0.03, 1600)
x = np.sin(2 * np.pi * 200 * t + 0)

axs[0].plot(t, x, color='darkviolet')

s = np.sin(2 * np.pi * 200 * t + 2)

axs[0].plot(t, s, color='darkorange')

s = np.sin(2 * np.pi * 200 * t + 4)

axs[0].plot(t, s, color='mediumslateblue')

s = np.sin(2 * np.pi * 200 * t + 6)

axs[0].plot(t, s, color='tomato')

z = np.random.normal(size=len(s))

xnorm = np.linalg.norm(x)
znorm = np.linalg.norm(z)

SNR = 0.1
gamma = np.sqrt((xnorm ** 2) / (SNR * znorm ** 2))

axs[1].plot(t, x + gamma * z, color='lightgray')

SNR = 1
gamma = np.sqrt((xnorm ** 2) / (SNR * znorm ** 2))

axs[1].plot(t, x + gamma * z, color='darkgray')

SNR = 10
gamma = np.sqrt((xnorm ** 2) / (SNR * znorm ** 2))

axs[1].plot(t, x + gamma * z, color='gray')

SNR = 100
gamma = np.sqrt((xnorm ** 2) / (SNR * znorm ** 2))

axs[1].plot(t, x + gamma * z, color='dimgray')

axs[1].plot(t, x, color='darkviolet')

plt.savefig('lab/02/ex2.pdf')
plt.show()