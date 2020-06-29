import random
from typing import *

class Card:
    # this method creates a card (an instance of the Card class)
    # each card should have a number and a suit
    def __init__(self, number: int, suit: str) -> "Card":
        self.number = number
        self.suit = suit
    
    # this method should take in a list of cards and add them up
    # based on their self.number attribute and return an int
    # value
    def add_cards(self, card_list: List["Card"]) -> int:
        for card in card_list:
            print("hi")
        return 0
    
    # this function should be able to print out a card
    # in the for "Ace of Spades" if given number = 1
    # and suit = "Spade"
    def __str__(self):
        if (self.number == 11):
            return "Jack of %s" % (self.suit)
        if (self.number == 12):
            return "Queen of %s" % (self.suit)
        if (self.number == 13):
            return "King of %s" % (self.suit)
        if (self.number == 1):
            return "Ace of %s" % (self.suit)
        return "%d of %s" % (self.number, self.suit)

class Deck:
    # this function creates a deck (an instance of the deck class)
    # and provides the deck capacities that a deck should have
    # e.g. a list of cards in the deck, a list of cards outside of
    # the deck, and perhaps a boolean telling us if the deck is 
    # empty. The attributes are not, however, limited to these
    def __init__(self) -> "Deck":
        numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        deck = []
        for s in suits:
            for n in numbers:
                cur_card = Card(n, s)
                deck.append(cur_card)
        self.deck = deck
        self.deck_size = 52
        self.empty = False
        self.discard = []
    
    # this function returns a list with the drawn cards. Undrawn
    # remain in the deck and the drawn are discarded
    def draw(self, n: int) -> List[Card]:
        if (self.deck_size < n):
            print("deck is empty")
            return None
        drawn = []
        while n > 0:
            drawn.append(self.deck.pop())
            n = n - 1
            self.deck_size = self.deck_size - 1
        self.discard = self.discard + drawn
        print(self.deck_size)
        return drawn
    
    # this function should 
    def shuffle(self) -> "Deck":
        deck = self.deck
        baseline = 2
        for n in range(2, self.deck_size):
            c1 = random.randint(baseline, n)
            c2 = random.randint(1, baseline)
            temp = deck[c1]
            deck[c1] = deck[c2]
            deck[c2] = temp
            baseline += 1
    
    # this is a 
    def print(self):
        for card in self.deck:
            print(card)
    
    
    
    def __str__(self) -> List[Card]:
        return "\n".join(print(x) for x in self.deck)
    
    def get_deck(self):
        return self.deck
    
    def get_discard(self):
        return self.discard
    
    def get_empty(self):
        return self.empty

### test code

deck = Deck()
deck.print()
print("If I draw 5 cards from an unshuffled deck, I draw")
for c in deck.draw(5):
    print(c)
print("now we shuffle")
deck.shuffle()
print("if we draw again, we draw")
for c in deck.draw(10):
    print(c)
print(deck)