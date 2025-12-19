import sounddevice as sd
import numpy as np

duration = 3  # seconds
fs = 16000

print("Speak now...")
myrecording = sd.rec(int(duration * fs), samplerate=fs, channels=1)
sd.wait()
print("Recorded audio shape:", np.shape(myrecording))
