from .thing             import Thing
from .mixins.located    import Located
from .mixins.containing import Containing

class Button(Thing):

    """a Button is a thing that interact with player"""

    #--------------------------------------------------------------------------
    # initialization
    #--------------------------------------------------------------------------

    def __init__(self, **kargs):
        super().__init__(**kargs)


    def init_from_yaml(self, data, world):
        super().init_from_yaml(data, world)

    def update_from_yaml(self, data, world):
        super().update_from_yaml(data, world)

    #--------------------------------------------------------------------------
    # API for saving the dynamic part of objects to YAML (via JSON)
    #--------------------------------------------------------------------------

    def archive_into(self, obj):
        super().archive_into(obj)

    #--------------------------------------------------------------------------
    # model API
    #--------------------------------------------------------------------------

    def is_button(self):
        return True


