from .holder import Holder

class Player(Holder):
    _type = 'player'

    def __init__(self, setPid, setName):
        self.hand = []
        #  super(Holder, self).__init__()
        self.pid = setPid
        self.name = setName
