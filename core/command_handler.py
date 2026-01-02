# core/command_handler.py
from utils.audio_helper import speak
from features.timers_reminders.timer_manager import TimerManager



timer_manager = TimerManager()


def handle(command: str):
    """
    Routes user commands to the appropriate feature.
    """

    command = command.lower().strip()

    # ---- TIMER COMMAND (Option A: strict) ----
    if command.startswith("set a timer for"):
        success, message = timer_manager.handle_timer_command(command)
        speak(message)
        return

    # ---- FALLBACK ----
    speak("Sorry, I don't know how to do that yet.")
