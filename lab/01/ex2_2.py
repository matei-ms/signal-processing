import numpy as np
import matplotlib.pyplot as plt

fig, axs = plt.subplots(1, 2)
fig.suptitle('Semnale 2d')

arr = np.random.rand(128, 128)

axs[0].imshow(arr, cmap='plasma')

def f(x, y):
  return np.sin(x / y) * np.cos(x * y)

arr = np.fromfunction(f, shape=(128,128))

axs[1].imshow(arr, cmap='viridis')

plt.savefig('lab/01/ex2_2.pdf')
plt.show()