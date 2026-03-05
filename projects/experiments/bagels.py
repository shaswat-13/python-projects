import random

# Generate a random 3-digit number
def random_number():
    return random.randint(100, 999)

# Display instructions
def display_instructions():
    print("\nWelcome to Bagels!!!")
    print("\nYou must guess a secret 3-digit number based on the clues.")
    print("Clues:")
    print("- Pico: A correct number in the wrong place.")
    print("- Fermi: A correct number in the correct place.")
    print("- Bagels: No correct numbers.")
    print("\nYou have 10 tries to guess the secret number.\n")

# Check clues
def check_clues(guess, actual):
    clues = []

    for i in range(len(guess)):
        if guess[i] == actual[i]:
            clues.append("Fermi")
        elif guess[i] in actual:
            clues.append("Pico")

    if not clues:
        clues.append("Bagels")
    
    clues.sort()
    return " ".join(clues)

# Main game loop
def play_game():
    display_instructions()
    secret_number = str(random_number())
    attempts_left = 10

    while attempts_left > 0:
        guess = input(f"{11 - attempts_left}. Enter your guess (3 digits): ")
        
        if len(guess) != 3 or not guess.isdigit():
            print("Invalid input. Please enter a 3-digit number.")
            continue
        
        if guess == secret_number:
            print(f"Correct! The number was {secret_number}. You win!\n")
            break

        # Provide clues
        clues = check_clues(guess, secret_number)
        print(clues)
        attempts_left -= 1

    if attempts_left == 0:
        print(f"You're out of attempts! The number was {secret_number}.\n")

# Loop to replay the game
while True:
    play_game()
    replay = input("Do you want to play again? (y/n): ").strip().lower()
    if replay != "y":
        print("Thanks for playing Bagels!")
        break
