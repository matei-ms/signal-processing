import numpy as np
import matplotlib.pyplot as plt

fig, axs = plt.subplots(4)
fig.suptitle('Exercițiul 1')

B = 1

t = np.linspace(-3, 3, 1000)
x = np.sinc(B * t) ** 2

fss = [1, 1.5, 2, 4]



plt.savefig('lab/06/ex1.pdf')
plt.show()