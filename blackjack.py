from deck import *

# this method should take in a list of cards and add them up
# based on their self.number attribute and return an int
# value
def add_cards(card_list: List["Card"]) -> int:
    ret_val = 0
    for card in card_list:
        ret_val += card.get_number()
    return ret_val

def end_game():
    #end the game, print the hands
    return None

def main():
    print("Let's play a game of BlackJack\n")
    playdeck = Deck()
    playdeck.shuffle()
    print("How many players are there?\n")
    n_players = input("number = ")
    opponent_hands = []
    your_hand = []
    for p in range(int(n_players) - 1):
        opponent_hands.append(playdeck.draw(2))
    print("Your hand is ")
    for c in your_hand[-1]:
        print(c)
    
    # draw again
    while True:
        print("Would you like to draw another card?")
        draw_bool = input("\'Yes\' or \'No\'? ").lower()
        if draw_bool == "no":
            break
        elif draw_bool == "yes":
            your_hand = your_hand + playdeck.draw(1)
            if add_cards(your_hand) > 21:
                print("you lose")
                end_game()
            print("Your hand is\n")
            for c in your_hand:
                print(c)
            # opponents' turns
            for opponent in opponent_hands:
                if add_cards(opponent) < 21:
                    opponent.draw(1)
        else:
            print("type \'yes\' or \'no\' you bimbo\n")
    for i in range(len(opponent_hands)):
        print(opponent)

main()