from .event import Event3

class PunchWithEvent(Event3):
    NAME = ""
        
    def perform(self):
        self.inform("jumpWith")
