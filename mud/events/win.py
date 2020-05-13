from .event import Event1

class WinEvent(Event1):
    NAME = "win"

    def perform(self):
        self.inform("win")
        self.actor.move_to(None)
