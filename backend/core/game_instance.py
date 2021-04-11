import random
from .player import Player
from .deck import Deck
from .field import Field
from .card import Card
from collections import Counter

class GameInstance:
    deck = None
    field = None
    players = None

    def __init__(self):
        self.deck = Deck()
        self.field = Field()
        self.players = {}

    def addPlayer(self, pid, name):
        #  print('ADDING: ' + pid)
        self.players[pid] = Player(pid, name)

    def removePlayer(self, pid):
        player = self.players.pop(pid, Player())
        self.deck.hand += player.hand
    
    def initialize(self, pidList):
        for pid in pidList:
            self.players[pid].hand = []
        self.deck.hand = [Card(i) for i in range(52)]
        self.shuffle('_deck')
        #  print(self.deck.hand)
        return { 'action': 'none', 'state': self.getState() }

    ## {'players': { 'use1': 10, 'user2': 3}, '_field': 3, '_deck':x}
    def getState(self):
        response = {}
        for pid, player in self.players.items():
            response[pid] = len(player.hand)
        response['_field'] = len(self.field.hand)
        response['_deck'] = len(self.deck.hand)
        return response


    def shuffle(self, target) :
        if (target == '_deck') :
            random.shuffle(self.deck.hand)
        elif (target == '_field') :
            random.shuffle(self.field.hand)
        else:
            random.shuffle(self.players["uid"].hand)


    def deal(self, count):
        messages = {}
        for pid in self.players.keys():
            messages[pid] = self.draw(pid, int(count), False)[0]
        return (messages, self.getState())


    #First is a boolean (if true, then player 1 is giving the card to player 2)
    def play(self, source: str, target: str, value: list):
        s = None
        if source == '_deck':
            s = self.deck.hand
        elif source == '_field':
            s = self.field.hand
        else:
            s = self.players[source].hand
        
        t = None
        if target == '_deck':
            t = self.deck.hand
        elif target == '_field':
            t = self.field.hand
        else:
            t = self.players[source].hand
        
        transfer = [card for card in s if card.uid in value]
        s = [card for card in s if card.uid not in value]
        t += transfer

        transfer = [card.serialize() for card in transfer]

        return (
            { 'action': 'remove', 'value': transfer },
            { 
                'action': 'add', 
                'target': target, 
                'value': transfer, 
                'state': self.getState() 
            }
        )

    def draw(self, target, numCard, withState=True):
        numCard = int(numCard)
        t = None
        if t == '_deck':
            t = self.deck.hand
        elif target == '_field':
            t = self.field.hand
        else:
            t = self.players[target].hand
        
        transfer = self.deck.hand[:numCard]
        self.deck.hand = self.deck.hand[numCard:]
        t += transfer

        transfer = [card.serialize() for card in transfer]

        return (
            { 'action': 'add', 'value': transfer },
            { 'action': 'none', 'state': self.getState() if withState else None }
        )
        

