from deckofcards import *
import random

class PokerPlayer(Player):
    def __init__(self, name, balance):
        super().__init__(name)
        self.balance = balance

class OpponentPlayer(PokerPlayer):
    pass

def generatePlayers(num, balance):
    players = []
    for i in range(num):
        players.append(PokerPlayer(str(i), balance))
    return players

def generateDeck():
    deck = Deck()
    deck.generate()
    return deck




starting_balance = 100
players = generatePlayers(2, starting_balance)
for i in range(len(players)):
    print(players[i].name)
    print(players[i].balance)

deck = generateDeck()

#Discard Pile
discard_pile = Deck()

