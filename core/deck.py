import Holder

class Deck(Holder):
    deckNumber = ''
    _type = 'deck'
    def __init__(self, setDeckNumber):
        super(Holder, self).__init__()
        deckNumber = setDeckNumber