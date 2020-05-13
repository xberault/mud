from .event import Event3

class GiveEvent(Event3):
    NAME = "give"
        
    def perform(self):
        object1 = self.context()["object"]
        recipient = self.context()["object2"]
        
        if not object1.has_prop("giveable"):
            object1.add_prop("give.failed")
            self.fail()
            return
        if not recipient.has_prop("receiver"):
            recipient.add_prop("give.failed")
            self.fail()
            return
        object1.move_to(recipient.container())
        self.inform("give")
        
