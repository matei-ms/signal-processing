import numpy as np
import sounddevice as sd

fs = 44100

t = np.arange(0, 1, 1 / fs)
s1 = np.sin(2 * np.pi * fs / 2 * t)
s2 = np.sin(2 * np.pi * fs / 4 * t)
s3 = np.sin(2 * np.pi * 0 * t)

sd.play(s1, fs)
sd.wait()
sd.play(s2, fs)
sd.wait()
sd.play(s3, fs)
sd.wait()

# pentru s1 si s3 e doar liniste; s3 este FOARTE high-pitched