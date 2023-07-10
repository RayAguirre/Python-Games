from deckofcards import *
import random
class PokerPlayer(Player):
    def __init__(self, name, balance):
        super().__init__(name)
        self.balance = balance
        self.currentBet = 0
        self.isOpponent = False

        #Player States
        self.dealer = False
        self.theirTurn = False
        self.folded = False
        self.called = False
        self.canRaise = False
        self.bigBlind = False
        self.smallBlind = False
    
    def doTurn(self, table, highestCall):
        if self.folded == True:
            return
        print("Hello " + str(self.name) + ". It is your turn.")
        #How much money they need to put in the pot
        total = 0
        if self.smallBlind == True:
            total += SMALL_BLIND
        if self.bigBlind == True:
            total += BIG_BLIND

        #Calling
        if self.called == False:
            choice = int(input("Call? 0 for Yes, 1 for No (Fold)"))
            if choice == 0:
                self.called = True
                total += highestCall - self.currentBet
                if self.balance < total:
                    print("You can't afford this! You must fold.")
                    self.folded = True
                    return
                else:
                    #Updates balances
                    self.balance -= total
                    table.pot += total
                    self.currentBet = self.currentBet + total
                    self.canRaise = True
                    total = 0
            elif choice == 1:
                self.called = True
                self.folded = True
                return

        if self.called == True:
            #Ask to Check, Fold, or Raise
            choice = int(input("Check, Raise, or Fold? 0 for Check, 1 for Fold, 2 for Raise"))
            if choice == 0:
                return
            elif choice == 1:
                self.folded = True
                return
            elif choice == 2 and self.canRaise == True:
                amt_raise = str(input("How much do you want to raise?"))
                while amt_raise > self.balance:
                    amt_raise = str(input("Not enough funds to raise this amount."))
                total += amt_raise

                #Update balances
                self.balance -= total
                table.pot += total
                table.highestCall = total
                self.currentBet = self.currentBet + total
                return

class OpponentPlayer(PokerPlayer):
    def __init__(self, name, balance):
        super().__init__(name, balance)
        self.isOpponent = True

def generatePlayers(num, balance):
    players = []
    max_players = 6

    #Ask again if they input more than max_players
    while num > max_players or num <= 0:
        print("Sorry. Please choose between 1-6 players.")
        num = int(input("How many players?"))

    for i in range(num):
        players.append(PokerPlayer("Player " + str(i + 1), balance))

        # Human Player
        if i == 0:
            name = input("What is your name?")
            players[i].name = name
            print("Welcome " + name)
        else:
            players[i] = OpponentPlayer(players[i].name, players[i].balance)
    return players

def generateDeck():
    deck = Deck()
    deck.generate()
    return deck

class Table:
    def __init__(self, players):
        tableOrder = players
        self.community = PokerPlayer("Table", 0)
        self.pot = 0
        self.round = 0
        self.highestCall = 0

    def generateTableOrder(self, players):
        for i in range(len(players)-1, 0, -1):
            r = random.randint(0, i)
            players[i], players[r] = players[r], players[i]
        return players
    
    def viewTable(self, players):
        print("Round: " + str(self.round))
        print("---")
        for i in range(len(players)):
            print(players[i].name)
            print(players[i].balance)
            print(players[i].isOpponent)
            print("Their Turn: " + str(players[i].theirTurn))
            print("Dealer: " + str(players[i].dealer))
            print("Small Blind: " + str(players[i].smallBlind))
            print("Big Blind: " + str(players[i].bigBlind))
            print("Folded: " + str(players[i].folded))
            print("Called: " + str(players[i].called))
            print("Can Raise: " + str(players[i].canRaise))
            print("Cards: ")
            players[i].showHand()
            print("---")

    def initRound(self):
        self.round += 1
        if len(self.tableOrder) == 1:
            self.tableOrder[0].smallBlind = True
        elif len(self.tableOrder) == 2:
            self.tableOrder[0].smallBlind = True
            self.tableOrder[1].bigBlind = True
        else:
            self.tableOrder[0].smallBlind = True
            self.tableOrder[1].bigBlind = True
            self.tableOrder[len(self.tableOrder) - 1].dealer = True

    def dealHole(self, deck):
        for i in range(2):
            for j in range(len(self.tableOrder)):
                self.tableOrder[j].draw(1, deck)

    def dealFlop(self, deck):
        self.community.draw(3, deck)
    
    def dealTurn(self, deck):
        self.community.draw(1, deck)
    
    def dealRiver(self, deck):
        self.community.draw(1, deck)

    def bettingRound(self):

        #One Full Round of Betting
        for i in range(len(self.tableOrder)):
            self.tableOrder[i].theirTurn = True
            self.tableOrder[i].doTurn(self, self.highestCall)
            self.updateTable()
            self.tableOrder[i].theirTurn = False

        #If a player hasn't called and hasn't folded, restart.
        for i in range(len(self.tableOrder)):
            if (self.tableOrder[i].called == False) and (self.tableOrder[i].folded == False):
                self.bettingRound()
            else:
                continue
    
    def updateTable(self):
        #Update Player States
        for player in self.tableOrder:
            if player.folded == True:
                continue
            if player.currentBet >= self.highestCall:
                self.highestCall = player.currentBet
            elif player.currentBet < self.highestCall:
                player.called = False

    def endRound(self, discard):
        # Switch Order Around
        if len(self.tableOrder) > 1:
            element = self.tableOrder.pop(0)
            self.tableOrder.append(element)
            self.resetStates()

        # Discards All Cards, Puts Them in Discard Pile
        for p in self.tableOrder:
            p.discardHand(discard)
        self.community.discardHand(discard)
    
    def resetStates(self):
        for i in range(len(self.tableOrder)):
            self.tableOrder[i].theirTurn = False
            self.tableOrder[i].folded = False
            self.tableOrder[i].called = False
            self.tableOrder[i].canRaise = False
            self.tableOrder[i].bigBlind = False
            self.tableOrder[i].smallBlind = False
            self.tableOrder[i].dealer = False
"-------------------------------"
#SET STARTING BALANCE
starting_balance = 100
SMALL_BLIND = 10
BIG_BLIND = 20

#Generate Players
players = generatePlayers(30, starting_balance)

deck = generateDeck()
deck.shuffle()

#Discard Pile
discard_pile = Deck()

#Create Table and Randomly Generate Table Order
table = Table(players)
table.tableOrder = table.generateTableOrder(players)
table.initRound()
table.viewTable(players)

table.endRound(discard_pile)
table.viewTable(players)

table.initRound()
table.viewTable(players)

table.dealHole(deck)
table.viewTable(players)
deck.count()

table.dealFlop(deck)
table.bettingRound()

table.dealTurn(deck)
table.dealRiver(deck)
table.community.showHand()
deck.count()

table.endRound(discard_pile)
table.community.showHand()
table.viewTable(players)
deck.count()
discard_pile.count()
