'''The base Game class, used to handle different games' different APIs.

This file defines the abstract Game class, with very few implemented attributes.
Due to the wide variety of APIs, each game should have it's own Game implementation

All necessary methods and variables are defined here.

created 2019-02-09 by NGnius '''

class Game:
    def __init__(self, name, *args, **kwargs):
        ''' initialise the Game instance '''

        '''self.names:
        aliases of the Game's name
        eg Call Of Duty 2, COD2, Call of Duty II '''
        self.names = list() # list of str

        '''self.name:
        official name of the Game
        eg COD2's name is "Call of Duty 2" '''
        self.name = name # str

        '''self.refresh_period:
        period between token refreshes
        ie every self.refresh_period seconds, self.refresh_token will be called '''
        self.refresh_period = int() # int -- seconds

    async def get_player(id=None, name=None):
        return # return Player

    async def refresh_token():
        return

    async def connect():
        return
