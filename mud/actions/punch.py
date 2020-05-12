from .action import Action3
from mud.events import PunchWithEvent

class PunchWithAction(Action3):
    EVENT = PunchWithEvent
    RESOLVE_OBJECT = "resolve_for_operate"
    RESOLVE_OBJECT2 = "resolve_for_use"
    ACTION = "punchWith"
    
    
    