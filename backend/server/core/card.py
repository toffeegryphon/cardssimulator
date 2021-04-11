SUITS = ['Spades', 'Hearts', 'Clubs', 'Diamonds']
RANKS = {0: "Ace", 10: "Jack", 11: "Queen", 12: "King"}

class Card:
    def __init__(self, uid):
        self.uid = uid
        self.suit = uid // 13
        self.rank = uid - self.suit * 13

    
    def serialize(self):
        return {
            "uid": self.uid, 
            "suit": SUITS[self.suit], 
            "value": RANKS.get(self.rank, self.rank + 1)
        }

    def __str__(self):
        return str(self.uid)

    def __repr__(self):
        return str(self.uid)
