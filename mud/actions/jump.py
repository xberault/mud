from .action import Action1
from mud.events import JumpEvent

class JumpAction(Action1):
    EVENT = JumpEvent
    ACTION = "jump"
