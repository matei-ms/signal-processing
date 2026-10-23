import numpy as np
import sounddevice as sd
import scipy.io

fs = 44100

t = np.arange(0, 1, 1 / 44100)
s = np.sin(2 * np.pi * 400 * t)

sd.play(s, 44100)
sd.wait()

t = np.arange(0, 3, 1 / 44100)
s = np.sin(2 * np.pi * 800 * t)

sd.play(s, 44100)
sd.wait()

t = np.arange(0, 1, 1 / 44100)
s = 2 * (t * 240 - np.floor(t * 240)) - 1

sd.play(s, 44100)
sd.wait()

t = np.arange(0, 1, 1 / 44100)
s = np.sign(np.sin(2 * np.pi * 300 * t))

sd.play(s, 44100)
sd.wait()

rate = int(10e5)
scipy.io.wavfile.write('lab/02/ex3.wav', rate, s)
rate, x = scipy.io.wavfile.read('lab/02/ex3.wav')

sd.play(x, fs)
sd.wait()