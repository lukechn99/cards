from deck import *

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
        elif draw_bool == "yes":
            player_hands[-1] = player_hands[-1] + playdeck.draw(1)
            print("Your hand is\n")
            for c in player_hands[-1]:
                print(c)
            # opponents' turns
            # for opponent in range(n_players - 1):
            #     player_hands[opponent]
        else:
            print("type \'yes\' or \'no\' you bimbo\n")

main()