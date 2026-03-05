import random

# generate random number
actual_number = random.randint(1,100)

# loop until user enters a valid number
def get_number(guess):
    while True:
        print(f'You have {guess} guesses left. Take a guess.')
        num = input('> ')

        if num.isdigit():
            if (1 <= int(num) <= 100):
                return int(num)

        print('Please enter a valid number.')
        
# provide feedback if the number was correct or not
def is_correct(guess):
    if guess == actual_number:
        return True
    elif guess < actual_number:
        print('Your guess is too low!')
    else:
        print('Your guess is too high!')
    return False

# main function
def main():

    print('\nI am guessing of a number between 1 and 100')

    # loop until all the guesses are done
    num_guesses = 10
    while num_guesses != 0:

        guessed_num = get_number(num_guesses)

        if is_correct(guessed_num):
            print('Yay! You guessed my number! \n')
            break

        num_guesses -=1

    # if ran out of guess
    if num_guesses == 0:
        print(f'Game Over. The number i was thinking of was {actual_number}\n')

if __name__ == '__main__':
    main()