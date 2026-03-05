import random

def show_instructions():
    print("Welcome to Blackjack!")
    print("The goal is to get as close to 21 as possible without going over.")
    print("You will be dealt two cards, and you can choose to hit (get another card) or stand (keep your current hand).")
    print("If you go over 21, you lose. If you have a higher total than the dealer without going over 21, you win!")
    print("Good luck!")

# get a shuffled deck of cards
def shuffle_deck():
    suits = ['heart', 'spade', 'diamond', 'club']
    num_cards = [i for i in range(2,11)]
    face_cards = ['J', 'Q', 'K', 'A']
    cards = num_cards + face_cards
    deck = [(suit, card) for suit in suits for card in cards]
    random.shuffle(deck)
    return deck

# get the value of a card
def get_card_value(card):
    if card[1] in ['J', 'Q', 'K']:
        return 10
    elif card[1] == 'A':
        return 11
    elif card.isdigit():
        return card[1]
    else:
        return None


def calculate_hand_value(hand):
    value = 0
    aces = 0
    for card in hand:
        card_value = get_card_value(card)
        if card_value == 11:
            aces += 1
        value += card_value

    while value > 21 and aces:
        value -= 10
        aces -= 1

    return value




def main():
    show_instructions()
    deck = shuffle_deck()
    player_hand = [deck.pop(), deck.pop()]
    dealer_hand = [deck.pop(), deck.pop()]

    print(f"Your hand: {player_hand}")
    print(f"Dealer's hand: {dealer_hand[0]}, ?")

    while True:
        action = input("Do you want to hit or stand? (h/s): ").lower()
        if action == 'h':
            player_hand.append(deck.pop())
            print(f"Your hand: {player_hand}")
            if calculate_hand_value(player_hand) > 21:
                print("You busted! Dealer wins.")
                return
        elif action == 's':
            break
        else:
            print("Invalid input. Please enter 'h' or 's'.")

    while calculate_hand_value(dealer_hand) < 17:
        dealer_hand.append(deck.pop())

    print(f"Dealer's hand: {dealer_hand}")

    player_value = calculate_hand_value(player_hand)
    dealer_value = calculate_hand_value(dealer_hand)

    if dealer_value > 21 or player_value > dealer_value:
        print("You win!")
    elif player_value < dealer_value:
        print("Dealer wins!")
    else:
        print("It's a tie!")

if __name__ == "__main__":  
    main()
