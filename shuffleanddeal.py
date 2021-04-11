import random

class GameInstance:
    deck = Holder()
    field = Holder()
    players = {
    'uid' : Holder()
    }

    def __init__(self):
        deck.hand = [Card(i) for i in range(52)]

    def shuffle(self, target) :
        if (target == 'deck') :
            random.shuffle(deck.hand)
        elif (target == 'field') :
            random.shuffle(field.hand)
        else:
            random.shuffle(players["uid"].hand)


    def deal(self, count, player, deck):
        for number in range(count):
            removed_value = random.choice(deck.hand)
            deck.remove(removed_value)
            player.hand.append(removed_value)
