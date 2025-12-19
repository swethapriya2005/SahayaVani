import json
from vosk import Model, KaldiRecognizer
import pyaudio

model = Model("models/vosk-telugu")
recognizer = KaldiRecognizer(model, 16000)

def speech_to_text():
    mic = pyaudio.PyAudio()
    stream = mic.open(
        format=pyaudio.paInt16,
        channels=1,
        rate=16000,
        input=True,
        frames_per_buffer=8192
    )
    stream.start_stream()

    print("🎤 మాట్లాడండి...")
    while True:
        data = stream.read(4096, exception_on_overflow=False)
        if recognizer.AcceptWaveform(data):
            result = json.loads(recognizer.Result())
            return result.get("text", "")
