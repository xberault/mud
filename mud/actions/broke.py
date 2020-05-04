from .action import Action3
from mud.events import BrokeEvent

class BrokeAction(Action3):
    EVENT = BrokeEvent
    RESOLVE_OBJECT = "resolve_for_operate"
    RESOLVE_OBJECT2 = "resolve_for_use"
    ACTION = "broke"
    
    
    