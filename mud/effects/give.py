from .effect import Effect3
from mud.events import GiveEvent


class GiveEffect(Effect3):
    EVENT = GiveEvent
