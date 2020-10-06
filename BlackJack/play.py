from cards import Shuffle
from cards import Card
from cards import ranks,suits,values
from cards import playing
from hand import Hand,Chips


def take_bet(chips):

    while True:

        try:
            chips.bet = int(input("how many chips you bet"))

        except ValueError:
            print("sorry wrong input")


        else:
            if chips.bet > chips.total:
                print("you are misleading")

            else:
                break




def hit(deck,hand):
    single_card = deck.give_card()
    hand.add_sys(single_card)
    hand.adjust()




def show_some(player,dealer):
    print("\nDealer's Hand:")
    print(" <card hidden>")
    print('',dealer.cards[1])  
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    
def show_all(player,dealer):
    print("\nDealer's Hand:", *dealer.cards, sep='\n ')
    print("Dealer's Hand =",dealer.value)
    print("\nPlayer's Hand:", *player.cards, sep='\n ')
    print("Player's Hand =",player.value)





def hit_or_hand(deck,hand):
    global playing


    while True:
        x = input('input h or s')

        if x[0].lower() == 'h':
            hit(deck,hand)

        elif x[0].lower() == 's':
            print("dealer turn")
            playing = False

        else:
            continue

        break


def player_fuck(player,dealer,chips):
    print("busted")
    chips.loss()

def player_win(player,dealer,chips):
    print("you won")
    chips.win()

def dealer_fuck(player,dealer,chips):
    print("comp busted")
    chips.loss()

def dealer_win(player,dealer,chips):
    print("comp won")
    chips.win()

def push(player,dealer):
    print("tieees") 




while True:

    print("Welcome to blackjack")
    deck = Shuffle()
    deck.shuff

    player_hand = Hand()
    player_hand.add_sys(deck.give_card())
    player_hand.add_sys(deck.give_card())


    dealer_hand = Hand()
    dealer_hand.add_sys(deck.give_card())
    dealer_hand.add_sys(deck.give_card())


#Setting player chips


    player_chips= Chips()

#playr bets
    take_bet(player_chips)


#show Cards

    show_some(player_hand,dealer_hand)

########################################################################################################################
#Logic copied dont know black jack properly


    while playing:

        hit_or_hand(deck,player_hand)


        show_some(player_hand,dealer_hand)


        if player_hand.value > 21:
            player_fuck(player_hand,dealer_hand,player_chips)

    if player_hand.value <=21:

        while dealer_hand.value < 17:
            hit(deck,dealer_hand)


        show_all(player_hand,dealer_hand)


        if dealer_hand.value > 21:
            dealer_fuck(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value > player_hand.value:
            dealer_win(player_hand,dealer_hand,player_chips)

        elif dealer_hand.value < player_hand.value:
            player_win(player_hand,dealer_hand,player_chips)

        else:
            push(player_hand,dealer_hand)        
    
    # Inform Player of their chips total 
    print("\nPlayer's winnings stand at",player_chips.total)
    



#asking user if want to play

if input("do not want to play more type n") == 'n':
    False