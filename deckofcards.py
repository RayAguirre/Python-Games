import random
class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def show(self):
        print("{} of {}".format(self.value, self.suit))

class Deck:
    def __init__(self):
        self.cards = []
        print("Created new deck.")
    
    def generate(self):
        for s in ["S", "C", "D", "H"]:
            for v in range(1, 14):
                self.cards.append(Card(v, s))
    
    def shuffle(self):
        for i in range(len(self.cards)-1, 0, -1):
            r = random.randint(0, i)
            self.cards[i], self.cards[r] = self.cards[r], self.cards[i]

    def print(self):
        for card in self.cards:
            card.show()

    def count(self):
        print(len(self.cards))

    def draw(self):
        return self.cards.pop()

class Player():
    def __init__(self):
        self.hand = []
    
    def draw(self, num, deck):
        for i in range(num):
            self.hand.append(deck.draw())

    def showHand(self):
        for c in self.hand:
            c.show()

def TestDeck():
    my_deck = Deck()
    my_deck.generate()
    my_deck.shuffle()
    my_deck.print()
    my_deck.count()
    p1 = Player()
    p1.draw(5, my_deck)
    p1.showHand()

# TestDeck()
