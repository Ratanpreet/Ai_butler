import speech_recognition as sr
import pyttsx3
from core.config import WAKE_WORD, MICROPHONE_INDEX

recognizer = sr.Recognizer()

def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()
    engine.stop()

def listen_for_wake_word():
    with sr.Microphone(device_index=MICROPHONE_INDEX) as source:
        print("Listening for wake word...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio).lower()
            if WAKE_WORD in command:
                print("Wake word detected!")
                speak("Hello, Master. How can I help you?")
                return True
        except sr.UnknownValueError:
            pass
        except sr.RequestError as e:
            print(f"Speech error: {e}")

        return False

def listen_for_command():
    with sr.Microphone(device_index=MICROPHONE_INDEX) as source:
        print("Listening for command...")
        recognizer.adjust_for_ambient_noise(source, duration=1)
        audio = recognizer.listen(source)

        try:
            command = recognizer.recognize_google(audio).lower()
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            print("Could not understand command.")
        except sr.RequestError as e:
            print(f"Speech error: {e}")

        return None

def main():
    while True:
        if listen_for_wake_word():
            command = listen_for_command()
            if command:
                speak(f"You said: {command}")

if __name__ == "__main__":
    main()
