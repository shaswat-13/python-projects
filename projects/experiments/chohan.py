# a japanese dice game
import random
import sys

jp_numbers = {1: 'Ichi', 2: 'Ni', 3: 'San', 4: 'Shi', 5: 'Go', 6: 'Roku'}


def display_instructions():
    instructions = '''Cho Han \n\nIn this traditional Japanese dice game, two dice are rolled in a bamboo cup\nby the dealer sitting on the floor. The player must guess if the\ndice totals to an even (cho) or odd (han) number.\n'''
    print(f'\n{instructions}\n')

def get_response(money):
    text = f'''\nYou have {money} mon.\nHow much do you want to bet?\nMinimum bet is 40. Type QUIT to quit'''
    while True:
        print(text)
        resp = input('> ')

        if resp.upper() == 'QUIT':
            print('\nThanks for playing')
            sys.exit()
        elif resp.isdigit():
            if (40 <= int(resp) <= money):
                return int(resp)
        print('Please enter valid mon!\n')

def get_cho_or_han():
    text = '''\nThe dealer swirls the cup and you hear the rattle of dice.\nThe dealer slams the cup on the floor, still covering the\ndice and asks for your bet.'''
    print(text)
    while True:
        print('\nCHO (if your guess is even) or HAN (if your guess is odd)')
        resp = input('> ')
        if ((resp.upper() == 'CHO') or (resp.upper() == 'HAN')):
            return  resp.upper() 
        print('Please enter a valid response')         

def dice_roll():
    return random.randint(1,6)

def did_win(choice):
    dice1 = dice_roll()
    dice2 = dice_roll()
    print(f'''\nThe dealer lifts the cup to reveal:\n{jp_numbers[dice1]} - {jp_numbers[dice2]}\n{dice1} - {dice2}''')
    sum = dice1 + dice2

    if (((sum % 2 == 0) and (choice == 'CHO')) or ((sum % 2 != 0) and (choice == 'HAN'))):
        return True
    else:
        return False



def main():
    display_instructions()
    
    total_money = 5000
    while True:
        bet = get_response(total_money)
        choice = get_cho_or_han()

        if(did_win(choice)):
            print(f'You won. You take {bet*2} mon.')
            total_money += 2*bet
        else:
            print(f'You lost!')
            total_money -= bet
        print(f'The house fee of {bet//10} mon has been deducted.')
        total_money -= bet//10

        if total_money <= 0:
            print('You are out of money')
            break


if __name__ == '__main__':
    main()