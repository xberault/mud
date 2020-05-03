from .action import Action1
from mud.events import BarkEvent

class BarkAction(Action1):
    EVENT = BarkEvent
    ACTION = "bark"
