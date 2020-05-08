from .event import Event2

class DrinkEvent(Event2):
    NAME = "drink"

    def perform(self):
        if not self.object.has_prop("drinkable"):
            self.fail()
            return self.inform("drink.failed")
        self.inform("drink")
