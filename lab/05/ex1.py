import numpy as np
import matplotlib.pyplot as plt
import datetime

x = np.genfromtxt('lab/05/Train.csv', delimiter=',', skip_header=1, usecols=2)

N = len(x)

# a.
fs = 1 / 3600 # 1 esantion / 1 ora

# b. 2 ani & 1 luna (se obs din Train.csv)
# print(N) = 18288 ore

# c. fs / 2 = 1 / 7200Hz

# d.
X = np.fft.fft(x)
X = abs(X / N)
X = X[:N // 2]

f = fs * np.linspace(0, N / 2, N // 2) / N

fig, axs = plt.subplots()
fig.suptitle('Modulul transformatei Fourier')

axs.plot(f, X, color='mediumvioletred')

axs.set_xlabel('Frecventa (Hz)')
axs.set_ylabel('|X(f)|')
axs.grid(True)

plt.savefig('lab/05/ex1_d.pdf')
# plt.show()

# e.
# din grafic => are componenta continua
# print(X[0]) ~= 139
medie = np.mean(x)
x = x - medie

X = np.fft.fft(x)
X = abs(X / N)
X = X[:N // 2] 
# print(X[0]) ~= 0

# f.
patru = np.argsort(X)[-4:][::-1]

for i in patru:
    print(f[i], X[i], 1 / f[i] / 3600)
# 1.1575339968646325e-05 27.10202228761556 23.997375328083987
# ^ ciclu zilnic
# celelalte 3 sunt ~= N, N/2, N/3
# ^ cresterea in timp a volumului de trafic

# g.
# print(datetime.date(2012, 8, 25).weekday()) = 5 = sambata
luni = 48 + 24 * 7 * 6
# print(luni) = 1056 > 1000

fig, axs = plt.subplots()
fig.suptitle('O lună de trafic')

axs.plot(np.arange(luni, luni + 24 * 30), x[luni:luni + 24 * 30] + medie, color='mediumvioletred')

axs.set_xlabel('Esantioane')
axs.set_ylabel('Nr masini')
axs.grid(True)

plt.savefig('lab/05/ex1_g.pdf')
# plt.show()

# h.
# vol de trafic din weekend este mai scazut, la fel si traficul de noapte
# => se pot deduce ziua saptamanii respectiv ora la care incepe masurarea
# zilele cu trafic neobisnuit de mic (/ mare; o locatie turistica are mai mult trafic) sunt probabil sarbatori
# daca stim exact ce sarbatori sunt in acel loc, stim si distanta dintre ele => ne dam seama care sarbatoare e care
# => ne dam seama de data la care incepe masurarea
# alaturi de ziua saptamanii ne putem da seama care este anul (totusi, ziua saptamanii se repeta la cativa ani)
# alt neajuns este ca daca nu stim locatia, nu stim exact ce sarbatori sunt
# este posibil si sa avem outliers din alte motive si sa ii confundam cu sarbatori

# i.
X = np.fft.fft(x)

f = fs * np.linspace(0, N / 2, N // 2) / N 