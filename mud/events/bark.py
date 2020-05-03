from .event import Event1

class BarkEvent(Event1):
    NAME = "bark"

    def perform(self):
        self.inform("bark.succeeded")
