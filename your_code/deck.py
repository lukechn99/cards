import random
from typing import *
# before running any code, decide on a case by case basis
# whether a function needs a 'return' statement or not
# the 'return None' and 'return 0's are there so the code
# will not break

class Card:
    # this method creates a card (an instance of the Card class)
    # each card should have a number and a suit
    def __init__(self, number: int, suit: str):
        # write your code here
        return None
    
    # this method should take in a list of cards and add them up
    # based on their self.number attribute and return an int
    # value
    def add_cards(self, card_list: List["Card"]) -> int:
        # write your code here
        return 0
    
    # the str method allows logical printing of an
    # abnormal object. Since here we are representing
    # the card as a Card, Card needs a special print
    # method
    # for example, we should get "Ace of Spades" if 
    # the given number = 1 and suit = "Spade"
    def __str__(self):
        # write your code here
        return None

class Deck:
    # this function creates a deck (an instance of the deck class)
    # and provides the deck capacities that a deck should have
    # e.g. a list of cards in the deck, a list of cards outside of
    # the deck, and perhaps a boolean telling us if the deck is 
    # empty. The attributes are not, however, limited to these
    def __init__(self) -> "Deck":
        # create code to make the deck and replace 'make me' with 
        # an actual deck
        self.deck = "make me"
        self.deck_size = 52
        self.empty = False
        self.discard = []
    
    # this function returns a list with the drawn cards. Undrawn
    # remain in the deck and the drawn are discarded
    def draw(self, n: int) -> List[Card]:
        # write your code here
        return None
    
    # this function should take in a deck, create a copy of it
    # use some sort of algorithm to shuffle the copy, and then
    # hand that back to self.deck
    def shuffle(self):
        # write your code here
        return None
    
    # this method should be able to be called on a deck. Without
    # this, print(myDeck) would result in an error (if myDeck is
    # your Deck) because Deck is not a printable type. Think about
    # how we can represent this
    def __str__(self):
        # write your code here
        return None
    
    # the below are freebies
    def get_deck(self):
        return self.deck
    
    def get_discard(self):
        return self.discard
    
    def get_empty(self):
        return self.empty

### test your code here! Some examples of tests you could do are...

# deck = Deck()
# deck.print()
# print("If I draw 5 cards from an unshuffled deck, I draw")
# for c in deck.draw(5):
#     print(c)
# print("now we shuffle")
# deck.shuffle()
# print("if we draw again, we draw")
# for c in deck.draw(5):
#     print(c)
# print(deck)