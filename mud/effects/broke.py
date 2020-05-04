
from .effect import Effect3
from mud.events import BrokeEvent


class BrokeEffect(Effect3):
    EVENT = BrokeEvent
