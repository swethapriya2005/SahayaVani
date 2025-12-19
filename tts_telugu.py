import pyttsx3

engine = pyttsx3.init()
engine.setProperty("rate", 150)

def speak(text):
    print("🔊 TELUGU:", text)
    engine.say(text)
    engine.runAndWait()
