from cards import Shuffle
from cards import Card
from cards import ranks,suits,values
from cards import playing

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0


    def add_sys(self,card):
        self.cards.append(card)
        self.value += values[card.rank]


        if card.rank == 'Ace':
            self.aces += 1
    

    def adjust(self):
        while self.value > 21 and self.aces > 0:
            self.value -= 10
            self.aces -= 1



class Chips:
        
    def __init__(self,total= 100):
        self.total = total
        self.bet = 0

    def win(self):
        self.total = self.total + self.bet

    def loss(self):
        self.total = self.total - self.bet


