import os
from dotenv import load_dotenv
load_dotenv(encoding="utf-8")


# Wake word configuration
WAKE_WORD = "hello" #not used anymore since we are using picovoice wake word

PICOVOICE_ACCESS_KEY = os.getenv("PICOVOICE_ACCESS_KEY")

WAKE_WORD_PATH = os.path.join("assets", "wake_words", "ramu_kaka.ppn")
# Audio settings
MICROPHONE_INDEX = 0  # Default microphone index
