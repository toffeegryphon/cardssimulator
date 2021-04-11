import random

class GameInstance:
    deck = Holder()
    field = Holder()
    players = {
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

    #First is a boolean (if true, then player 1 is giving the card to player 2)
    def play(self, player1, player2, field, deck, first):
        if (player2 == None):
            players_card = player1.Card
            player1.hand.remove(players_card)
            field.append(players_card)
        elif (first):
            move_card(player1, player2)
        else:
            move_card(player2, player1)

    def move_card(player1, player2):
        players_card = player1.Card
        player1.hand.remove(players_card)
        player2.append(players_card)
