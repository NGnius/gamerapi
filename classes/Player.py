'''The base Player class, used to store player information

This file implements all necessary Player methods and variables.
Due to the wide variety of APIs, some of these methods might need to be overriden

If more features are required, inherit from Player to extend it.
If Player is extended, one class per Game or GameDev is prefered.

created 2019-02-09 by NGnius'''

class Player:
    def __init__(id=None, *args, **kwargs):
        self.id = id
