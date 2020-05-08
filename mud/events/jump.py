from .event import Event1

class JumpEvent(Event1):
    NAME = "jump"
    
    def get_event_templates(self):
        return self.actor.container().get_event_templates()
        
    def perform(self):
        loc = self.actor.container()
        if not loc.has_prop("weak"):
            self.fail()
            return self.inform("jump.failed")
        self.inform("jump")
