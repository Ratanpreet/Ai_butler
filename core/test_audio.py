import pyaudio
import pvporcupine
import pyttsx3
import pyaudio

pa = pyaudio.PyAudio()
for i in range(pa.get_device_count()):
    info = pa.get_device_info_by_index(i)
    print(i, info["name"])

engine = pyttsx3.init()
engine.say("Python 3.11 setup successful")
engine.runAndWait()


print("Porcupine OK")
print("PyAudio is working")
