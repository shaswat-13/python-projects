import random

# declare global variables
suits = ['heart', 'spade', 'diamond', 'club']
ideal_list = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
mapping = {
            'trial': 5,
            'double_run': 4,
            'run': 3,
            'color': 2,
            'pair': 1,
            'high_card': 0
        }


class Card():
    # class members
    suit:str
    rank:str

    # initialize card class with suit and rank
    def __init__(self, pair:tuple):
        self.suit = pair[0]
        self.rank = pair[1]

    # display the card
    def __str__(self):
        return f"{self.rank} of {self.suit}"

class Hand():
    # class members
    cards:list[Card]
    high_card:str
    trial:bool
    trial_card:str
    run:bool
    run_cards:list[str]
    color:bool
    color_suit:str
    pair:bool
    pair_card:str
    double_run: bool
    double_run_suit: str
    max_hand_val:int
    max_hand: str
    sorted_hand: list[Card]
    sorted_hand_ranks: list[str]

    # initialize hand class with list of cards
    def __init__(self, cards:list[Card]):
        self.cards = cards

    # display the hand
    def __str__(self):
        return ', '.join(str(card) for card in self.cards)
    
    def sort_hand(self):
        self.sorted_hand = sorted(self.cards, key=lambda x: ideal_list.index(x.rank))
        self.sorted_hand_ranks = [card.rank for card in self.sorted_hand]
        print(f"Sorted hand: {self.sorted_hand_ranks}")

    
    # get the highest value card from the hand
    def get_max_card(self):
        self.high_card = self.sorted_hand_ranks[-1]
        print(f"High card of : {self.high_card}")
        
    # check if the hand has a trial and if so of which card
    def check_trial(self):
        list_of_ranks = [card.rank for card in self.cards]
        if len(set(list_of_ranks)) == 1:
            self.trial = True
            self.trial_card = self.cards[0].rank
            print(f"Trial of : {self.trial_card}")
        else:
            self.trial = False  
            self.trial_card = None

    # check if the hand has a color and if so of which suit
    def check_color(self):
        list_of_suits = [card.suit for card in self.cards]
        if len(set(list_of_suits)) == 1:
            self.color = True
            self.color_suit = self.cards[0].suit
            print(f"Color of : {self.color_suit}")
        else:
            self.color = False
            self.color_card = None
    
    # check if the hand has a pair and if so of which card
    def check_pair(self):
        list_of_ranks = [card.rank for card in self.cards]
        if len(list_of_ranks) == len(set(list_of_ranks)):
            self.pair = False
            self.pair_card = None
        else:
            self.pair = True
            for card in self.cards:
                if list_of_ranks.count(card.rank) == 2:
                    self.pair_card = card.rank
                    break
            print(f"Pair of : {self.pair_card}")

    # check if the hand has a run and if so of which card
    def check_run(self):
        if len(set(self.sorted_hand_ranks)) == 3:
            start_index = ideal_list.index(self.sorted_hand_ranks[0])
            if ideal_list[start_index:start_index+3] == self.sorted_hand_ranks or self.sorted_hand_ranks == ['2', '3', 'A']:
                self.run = True
                self.run_cards = self.sorted_hand_ranks.copy()
                print(f"Run of : {self.run_cards}")
                return
        self.run = False
        self.run_cards = None
        
    # check if the hand has a double run and if so of which suit and which cards
    def check_double_run(self):
        if self.color and self.run:
            self.double_run = True
            self.double_run_suit = self.color_suit
            print(f"Double run of : {self.double_run_suit} of {self.run_cards}")
        else:
            self.double_run = False
            self.double_run_suit = None
    
    # get the maximum priority of the hand (int value and name)
    def max_priority_and_hand(self):
        # get max hand int value
        if self.trial:
            max_hand = mapping['trial']
        elif self.double_run:
            max_hand = mapping['double_run']
        elif self.run:   
            max_hand = mapping['run']
        elif self.color:
            max_hand = mapping['color']
        elif self.pair:
            max_hand = mapping['pair']
        else:
            max_hand = mapping['high_card']
        self.max_hand_val = max_hand

        # get max hand name
        for key, value in mapping.items():
            if value == self.max_hand_val:
                self.max_hand = key
                break

    # check all the conditions of the hand
    def check_all(self):
        self.sort_hand()
        self.get_max_card()
        self.check_trial()
        self.check_run()
        self.check_color()
        self.check_double_run()
        self.check_pair()
        self.max_priority_and_hand()

# shuffle the deck
def shuffle_deck():
    deck = [(suit, card) for suit in suits for card in ideal_list]
    random.shuffle(deck)
    return deck

def check_for_winner(player_hand, computer_hand):
    if ideal_list.index(player_hand.high_card) > ideal_list.index(computer_hand.high_card):
        print("You win!")
    elif ideal_list.index(player_hand.high_card) < ideal_list.index(computer_hand.high_card):  
        print("Computer wins!")
    else:
        if ideal_list.index(player_hand.sorted_hand_ranks[-2]) > ideal_list.index(computer_hand.sorted_hand_ranks[-2]):
            print("You win!")
        elif ideal_list.index(player_hand.sorted_hand_ranks[-2]) < ideal_list.index(computer_hand.sorted_hand_ranks[-2]):
            print("Computer wins!")
        else:
            if ideal_list.index(player_hand.sorted_hand_ranks[-3]) > ideal_list.index(computer_hand.sorted_hand_ranks[-3]):
                print("You win!")
            elif ideal_list.index(player_hand.sorted_hand_ranks[-3]) < ideal_list.index(computer_hand.sorted_hand_ranks[-3]):
                print("Computer wins!")
            else:
                print("It's a tie!")

def main():
    # get the shuffled deck of list of Cards
    shuffled_deck = shuffle_deck()
    deck = list()
    for i in range(52):
        temp_card = shuffled_deck.pop()
        deck.append(Card(temp_card))

    # get the player and computer hands
    temp_p_hand = list()
    temp_c_hand = list()
    for i in range(3):
        card = deck.pop()
        temp_p_hand.append(card)

        card = deck.pop()
        temp_c_hand.append(card)

    player_hand = Hand(temp_p_hand)
    print(f"\nYour hand: {player_hand}")
    print('Player')
    player_hand.check_all()

    computer_hand = Hand(temp_c_hand)
    print(f"\nComputer's hand: {computer_hand}")
    print('Computer')
    computer_hand.check_all()
    
    print(f"\nPlayer has a {player_hand.max_hand} and computer has a {computer_hand.max_hand}\n")

    # check who wins
    if player_hand.max_hand_val > computer_hand.max_hand_val:
        print("You win!")
    elif player_hand.max_hand_val < computer_hand.max_hand_val:
        print("Computer wins!")
    else:
        # if both get trial
        if player_hand.max_hand_val == 5:
            if ideal_list.index(player_hand.trial_card) > ideal_list.index(computer_hand.trial_card):
                print("You win!")
            else:
                print("Computer wins!")
        
        # if both get double run
        elif player_hand.max_hand_val == 4:
            '''left to implement later'''
            check_for_winner(player_hand, computer_hand)

        # if both get run
        elif player_hand.max_hand_val == 3:
            '''left to implement later'''
            check_for_winner(player_hand, computer_hand)

        # if both get color
        elif player_hand.max_hand_val == 2:
            check_for_winner(player_hand, computer_hand)
        
        # if both get pair
        elif player_hand.max_hand_val == 1:
            if ideal_list.index(player_hand.pair_card) > ideal_list.index(computer_hand.pair_card):
                print("You win!")
            elif ideal_list.index(player_hand.pair_card) < ideal_list.index(computer_hand.pair_card):
                print("Computer wins!")
            else:
                check_for_winner(player_hand, computer_hand)

        # if both get high card
        elif player_hand.max_hand_val == 0:
            check_for_winner(player_hand, computer_hand)
            
if __name__ == "__main__":
    main()