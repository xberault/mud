from .effect import Effect3
from mud.events import PunchWithEvent


class PunchWithEffect(Effect3):
    EVENT = PunchWithEvent
