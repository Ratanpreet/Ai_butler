import pyttsx3

# Test TTS engine initialization
try:
    engine = pyttsx3.init()
    engine.say("Testing TTS engine. If you hear this, it's working.")
    engine.runAndWait()  # Speak immediately

    engine.say("Testing idk what is wrong 2. If you hear this, it's working.")
    engine.runAndWait()  # Speak immediately
except Exception as e:
    print(f"Error initializing TTS engine: {e}")
    exit()
