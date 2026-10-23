import numpy as np
import sounddevice as sd

fs = 44100

t = np.arange(0, 1, 1 / 44100)
s1 = np.sign(np.sin(2 * np.pi * 300 * t))
s2 = np.sign(np.sin(2 * np.pi * 1848 * t))

sd.play(np.concatenate([s1, s2]), 44100)
sd.wait()

# s2 este mai high-pitched