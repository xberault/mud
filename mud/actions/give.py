from .action import Action3
from mud.events import GiveEvent

class GiveAction(Action3):
    EVENT = GiveEvent
    RESOLVE_OBJECT = "resolve_for_use"
    RESOLVE_OBJECT2 = "resolve_for_operate"
    ACTION = "give"
    
    
    