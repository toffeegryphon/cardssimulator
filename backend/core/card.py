SUITS = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
RANKS = {0: "Ace", 10: "Jack", 11: "Queen", 12: "King"}

class Card:
    uid = 0
    isVisible = True
    rank = 0
    suit = 0

    def __init__(self, uid):
        self.uid = uid
        self.suit = uid // 13
        self.rank = uid - self.suit * 13

    
    def serialize(self):
        return {
            "uid": self.uid, 
            "suit": SUITS[self.suit], 
            "value": RANKS.get(self.rank, self.rank)
        }

    def __str__(self):
        return str(self.uid)

    def __repr__(self):
        return str(self.uid)
