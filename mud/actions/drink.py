from .action import Action2
from mud.events import DrinkEvent

class DrinkAction(Action2):
    EVENT = DrinkEvent
    RESOLVE_OBJECT = "resolve_for_operate"
    ACTION = "drink"
