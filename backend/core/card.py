SUITS = ['Spades', 'Hearts', 'Clubs', 'Diamonds']

class Card:
    uid = 0
    isVisible = True
    rank = ''
    suit = ''

    def __init__(self, uid):
        self.uid = uid
        self.suit = uid % 13
        self.rank = uid - self.suit * 13

    
    def serialize(self):
        specialCard = {0: "Ace", 10: "Jack", 11: "Queen", 12: "King"}
        rank_name = specialCard[self.rank] if self.rank in specialCard else self.rank
        return {
            "uid": self.uid, 
            "suit": SUITS[self.suit], 
            "value": self.value
        }

    def __str__(self):
        return str(self.uid)

    def __repr__(self):
        return str(self.uid)
