from .holder import Holder

class Deck(Holder):
    _type = 'deck'
    def __init__(self):
        super(Holder, self).__init__()
