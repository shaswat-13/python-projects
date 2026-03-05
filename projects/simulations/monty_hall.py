import random

# assign random prize to each door and store in a dict
doors = ['door1', 'door2', 'door3']
prizes = ['goat', 'goat', 'car']
random.shuffle(prizes)
door_inside = {door: prize for door, prize in zip(doors, prizes)}

# counter variables
stayWins = 0
stayLosses = 0
switchWins = 0
switchLosses = 0

# show instructions of the game
def display_instructions():
    print("\nWelcome to the Monty Hall Problem simulation!\n")
    print("You will be presented with three doors.")
    print("Behind one door is a car, and behind the other two are goats.")
    print("You will choose one door, and then the host will open another door that has a goat behind it.")
    print("You will then have the option to either stick with your original choice or switch to the other unopened door.")
    print("Let's see if you can win the car!\n")

# gets the first choice of the player
def get_valid_1st_choice():
    while True:
        choice = input("Choose a door (1, 2, or 3): ")
        if choice.isdigit() and int(choice) in [1, 2, 3]:
            return int(choice) - 1
        print("Invalid choice. Please choose a door (1, 2, or 3).")

# shows the door which wasnt chosen and has a goat behind it
def show_goat(door_chosen):
    print(f"Monty Hall will open one of the door that you didn't choose")

    for i in range(3):
        if i != door_chosen and door_inside[doors[i]] == 'goat':
            print(f"Door {i + 1} has been opened, revealing a goat.\n")
            return i

def choice_to_switch(door_chosen, door_opened):
    global stayWins, stayLosses, switchWins, switchLosses
    switch_choice = input("Do you want to switch your choice? (yes/no): ").strip().lower()
    
    if switch_choice == 'yes':
        for i in range(3):
            if i != door_chosen and i != door_opened:
                new_choice = i
                break
        print(f"You switched to door {new_choice + 1}.\n")
        if door_inside[doors[new_choice]] == 'car':
            print("Congratulations!!!!!!!!\nYou won the car!")
            switchWins += 1
        else:
            print("Sorry! You got a goat.")
            switchLosses += 1
    else:
        print(f"You stuck with door {door_chosen + 1}.")
        if door_inside[doors[door_chosen]] == 'car':
            print("Congratulations!!!!!!!!\nYou won the car!\n")
            stayWins += 1
        else:
            print("Sorry! You got a goat.")
            stayLosses += 1

    print(f"Stay Wins: {stayWins}, Stay Losses: {stayLosses}")
    print(f"Switch Wins: {switchWins}, Switch Losses: {switchLosses}")

def main():
    while True:
        display_instructions()
        first_choice = get_valid_1st_choice()
        print(f"You chose door {first_choice + 1}.\n")
        removed_door = show_goat(first_choice)
        choice_to_switch(first_choice, removed_door)
        print("\nDo you want to play again? (yes/no): ", end="")
        play_again = input().strip().lower()
        if play_again != 'yes':
            print("Thanks for playing!")
            break
        else:
            global door_inside
            # Reset the game state
            random.shuffle(prizes)
            door_inside = {door: prize for door, prize in zip(doors, prizes)}


if __name__ == "__main__":
    main()