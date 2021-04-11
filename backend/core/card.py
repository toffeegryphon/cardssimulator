class Card:
    uid = 0
    isVisible = True
    rank = ''
    suit = ''

    def __init__(self, id):
        uid = id
        suit = id % 13
        rank = id - suit * 13

    
    def serialize(self):
        specialCard = {0: "Ace", 10: "Jack", 11: "Queen", 12: "King"}
        rank_name = specialCard[self.rank] if self.rank in specialCard else self.rank
        return {"uid": self.uid, "suit": self.suit, "value": self.value}