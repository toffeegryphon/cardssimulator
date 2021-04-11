import random
import Player from 'player.py'
import Deck from 'deck.py'
import Field from 'field.py'

class GameInstance:
    deck = Deck()
    field = Field()
    players = {
    }

    def __init__(self):
        self.deck.hand = [Card(i) for i in range(52)]
    
    def initialize(self, pidList):
        for pid in pidList:
            self.players[pid] = Player()


    def shuffle(self, target) :
        if (target == 'deck') :
            random.shuffle(self.deck.hand)
        elif (target == 'field') :
            random.shuffle(self.field.hand)
        else:
            random.shuffle(self.players["uid"].hand)


    def deal(self, count):
        messages = {}
        for pid in self.players.keys():
            messages[pid] = draw(pid, count)
        return messages


    #First is a boolean (if true, then player 1 is giving the card to player 2)
    def play(self, source: str, target: str, value: list):
        s = None
        if source == 'deck':
            s = self.deck.hand
        elif source == 'field':
            s = self.field.hand
        else:
            s = self.players[source].hand
        
        t = None
        if target == 'deck':
            t = self.deck.hand
        elif target == 'field':
            t = self.field.hand
        else:
            t = self.players[source].hand
        
        transfer = [card for card in s if card.uid in value]
        s = [card for card in s if card.uid not in value]
        t += transfer

        return {
            source: { 'action': 'remove', 'value': transfer },
            target: { 'action': 'add', 'value': transfer }
        }

    def draw(self, target, numCard):      
        t = None
        if t == 'deck':
            t = self.deck.hand
        elif target == 'field':
            t = self.field.hand
        else:
            t = self.players[source].hand
        
        transfer = self.deck[:numCard]
        self.deck = self.deck[numCard:]
        t += transfer

        return { 'action': 'add', 'value': transfer }
        

