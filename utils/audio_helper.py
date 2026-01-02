# utils/audio_helper.py

import pyttsx3

def speak(text: str):
    engine = pyttsx3.init()
    engine.setProperty("rate", 170)
    engine.say(text)
    engine.runAndWait()
    engine.stop()
