from .holder import Holder

class Player(Holder):
    pid = ''
    name = ''
    _type = 'player'

    def __init__(self, setPid, setName):
        super(Holder, self).__init__()
        self.pid = setPid
        self.name = setName
