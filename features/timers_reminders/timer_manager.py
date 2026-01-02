# features/timers_reminders/timer_manager.py

import threading
import time
import re

from utils.audio_helper import speak

class TimerManager:
    def __init__(self):
        self.active_timer = None

    def handle_timer_command(self, command: str):
        """
        Expected format:
        'set a timer for 10 minutes'
        'set a timer for 30 seconds'
        """

        match = re.search(r"set a timer for (\d+) (second|seconds|minute|minutes)", command)

        if not match:
            return False, "Please say something like set a timer for 10 minutes."

        amount = int(match.group(1))
        unit = match.group(2)

        seconds = amount * 60 if "minute" in unit else amount

        if self.active_timer and self.active_timer.is_alive():
            return False, "A timer is already running."

        self.active_timer = threading.Thread(
            target=self._run_timer,
            args=(seconds,),
            daemon=True
        )
        self.active_timer.start()

        return True, f"Timer started for {amount} {unit}."

    def _run_timer(self, seconds: int):
        time.sleep(seconds)
        speak("Shaaaabji! Time's up!")
