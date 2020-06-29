import random

class Card:
    def __init__(self, number, suit):
        self.number = number
        self.suit = suit
        
    def add_cards(self, card_list):
        for card in card_list:
            print("hi")
    
    # this function should be able to print out a card
    # in the for "Ace of Spades" if given number = "1"
    # and suit = "Spade"
    def __str__(self):
        if (self.number == "11"):
            return "Jack of %s" % (self.suit)
        if (self.number == "12"):
            return "Queen of %s" % (self.suit)
        if (self.number == "13"):
            return "King of %s" % (self.suit)
        if (self.number == "1"):
            return "Ace of %s" % (self.suit)
        return "%s of %s" % (self.number, self.suit)

class Deck:
    def __init__(self):
        numbers = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13"]
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        deck = []
        for s in suits:
            for n in numbers:
                cur_card = Card(n, s)
                deck.append(cur_card)
        self.deck = deck
        self.empty = False
        self.discard = []
    
    # returns a list with the drawn cards, undrawn
    # remain in the deck and the drawn are discarded
    def draw(self, n):
        if (len(self.deck) <= n):
            print("deck is empty")
            return None
        drawn = []
        while n > 0:
            drawn.append(self.deck.pop())
            n = n - 1
        self.discard = self.discard + drawn
        return drawn
    
    # due to out of bound errors, the last 4 cards currently don't shuffle
    def shuffle(self):
        op_deck = self.deck
        baseline = 2
        for n in range(40):
            # c1 and c2 must always remain within 0 and 51
            c1 = random.randint(baseline + 1, n + 3)
            c2 = random.randint(1, baseline)
            temp = op_deck[c1]
            op_deck[c1] = op_deck[c2]
            op_deck[c2] = temp
            baseline += 1
    
    def print(self):
        for card in self.deck:
            print(card)
    
    def __str__(self):
        return None
    
    def get_deck(self):
        return self.deck
    
    def get_discard(self):
        return self.discard

def main():
    print("Let's play a game of BlackJack\n")
    playdeck = Deck()
    playdeck.shuffle()
    print("How many players are there?\n")
    n_players = input("number = ")
    player_hands = []
    for p in range(int(n_players)):
        player_hands.append(playdeck.draw(2))
    print("Your hand is ")
    for c in player_hands[-1]:
        print(c)
    
    # draw again
    while True:
        print("Would you like to draw another card?")
        draw_bool = input("\'Yes\' or \'No\'? ").lower()
        if draw_bool == "no":
            break
        else:
            player_hands[-1] = player_hands[-1] + playdeck.draw(1)
            print("Your hand is\n")
            for c in player_hands[-1]:
                print(c)
            # opponents' turns
            # for opponent in range(n_players - 1):
            #     player_hands[opponent]

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
main()