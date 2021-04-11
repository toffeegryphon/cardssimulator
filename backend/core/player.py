import Holder from 'holder.py'

class Player(Holder):
    pid = ''
    name = ''
    _type = 'player'
    def __init__(self, setPid, setName):
        super(Holder, self).__init__()
        pid = setPid
        name = setName
