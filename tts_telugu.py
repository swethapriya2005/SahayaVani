from gtts import gTTS
from playsound import playsound
import uuid
import os

def speak(text):
    print("🔊 TELUGU:", text)

    filename = f"telugu_{uuid.uuid4()}.mp3"
    tts = gTTS(text=text, lang="te")
    tts.save(filename)

    playsound(filename)
    os.remove(filename)
