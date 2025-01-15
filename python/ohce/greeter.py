from datetime import datetime
from abc import abstractmethod

class Clock:
    @abstractmethod
    def current_hour():
        pass

class SystemClock(Clock):
    def current_hour(self):
        now = datetime.now()
        return now.hour
    

class Greeter:
    def __init__(self, clock):
        self.clock = clock

    def greet(self):
        current_hour = self.clock.current_hour()
        if 6 <= current_hour < 12:
            return "Good morning"
        if 12 <= current_hour <= 19:
            return "Good afternoon"
        if current_hour >= 20 or current_hour < 6:
            return "Good night"
