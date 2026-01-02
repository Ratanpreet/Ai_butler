import struct
import pyaudio
import pvporcupine
import speech_recognition as sr

import time
from utils.audio_helper import speak

from core.config import (
    PICOVOICE_ACCESS_KEY,
    WAKE_WORD_PATH,
    MICROPHONE_INDEX
)
from core.command_handler import handle

# INITIALIZATIONS
recognizer = sr.Recognizer()




# Command listener
def listen_for_command() -> str | None:
    with sr.Microphone(device_index=MICROPHONE_INDEX) as source:
        print("🎤 Listening for command...")
        recognizer.adjust_for_ambient_noise(source, duration=0.5)
        audio = recognizer.listen(source)

    try:
        command = recognizer.recognize_google(audio).lower()
        print(f"🧠 Command: {command}")
        return command
    except sr.UnknownValueError:
        speak("Sorry, I did not understand that.")
    except sr.RequestError as e:
        print(f"STT Error: {e}")
        speak("Speech service error.")

    return None

# WAKE WORD LOOP 

def start_wake_word_listener():
    porcupine = pvporcupine.create(
        access_key=PICOVOICE_ACCESS_KEY,
        keyword_paths=[WAKE_WORD_PATH]
    )

    pa = pyaudio.PyAudio()

    audio_stream = pa.open(
        rate=porcupine.sample_rate,
        channels=1,
        format=pyaudio.paInt16,
        input=True,
        frames_per_buffer=porcupine.frame_length,
        input_device_index=MICROPHONE_INDEX
    )

    print("AI Butler is running. Say 'Ramu Kaka'...")

    try:
        while True:
            pcm = audio_stream.read(
                porcupine.frame_length,
                exception_on_overflow=False
            )

            pcm = struct.unpack_from(
                "h" * porcupine.frame_length,
                pcm
            )

            keyword_index = porcupine.process(pcm)

            if keyword_index >= 0:
                print("Wake word detected!")
                speak("Yes?")

                command = listen_for_command()
                
                if command:
                    time.sleep(0.1)
                    
                    handle(command)

    except KeyboardInterrupt:
        print("\nStopping assistant...")

    finally:
        audio_stream.close()
        pa.terminate()
        porcupine.delete()
        

# MAIN 

if __name__ == "__main__":
    start_wake_word_listener()
