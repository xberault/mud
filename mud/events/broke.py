from .event import Event3

class BrokeEvent(Event3):
    NAME = "broke"

    def get_event_templates(self):
        return self.actor.container().get_event_templates()
        
    def perform(self):
        object1 = self.context()["object"]
        object2 = self.context()["object2"]
        if not object2.has_prop("breaker"):
            self.fail()
            return self.inform("broke.failed.breaker")
        if not object1.has_prop("breakable"):
            self.fail()
            return self.inform("broke.failed.breakable")
        self.inform("broke")
