# an experiment to simulate the birthday paradox
import random

# store the months and their respective number of days  in a dict
month_and_days = {'Jan': 31, 'Feb': 28, 'Mar': 31, 'Apr': 30, 
                  'May': 31, 'Jun': 30, 'Jul': 31, 'Aug': 31,
                  'Sep': 30, 'Oct': 31, 'Nov': 30, 'Dec': 31}
months = list(month_and_days.keys())

# function to generate one random birthday
def generate_one_birthday():
    month = months[random.randint(0,11)]
    day = random.randint(1, month_and_days[month])
    return month + ' ' +str(day)
    
# run 1 simulation
def run_1_simulation(n):
    print(f'\nHere are {n} birthdays:\n')
    list_of_birthdays = list()
    while (n > 0):
        list_of_birthdays.append(generate_one_birthday())
        n -= 1

    print(list_of_birthdays)

    if has_duplicates(list_of_birthdays):
        # Initialize an empty set to store seen elements
        s = set()
        # List to store duplicates
        dup = list()
        for bd in list_of_birthdays:
            if bd in s:
                dup.append(bd)
            else:
                s.add(bd)
        print(f'\n\nIn this simulation, multiple people have birthdays on \n{dup}')

# returns true if there are duplicate values in a list
def has_duplicates(bd_list):
    return len(bd_list) != len(set(bd_list))

# run the simulation of generating n birthdays 100k times
def run_100k_simulations(n):

    # counter to store if a birthday was repeated in 1 simulation
    repeated_birthdays = 0

    sim = 1
    while True:
        # visual clue of how much simulations have been run so far
        if sim % 10000 == 0:
            print(f'{sim} simulations run...')

        # break if 100k simulations have been done
        elif sim == 100001:
            break
        
        # list to store random birthdays of 1 simulation
        list_of_birthdays = list()
        # times to generate the reqd number of random birthdays
        times = n
        while (times > 0):
            list_of_birthdays.append(generate_one_birthday())
            times -= 1
        if has_duplicates(list_of_birthdays):
            repeated_birthdays += 1
        
        # increase the simulation count after each iteration
        sim += 1

    # Display the result of the simulation    
    print(f'\nOut of 100,000 simulations of {n} people,\nthere was a matching birthday in that group {repeated_birthdays} times.')
    perc = round((repeated_birthdays/100000) * 100,2)
    print(f'This means that {n} people have a {perc}% chance of having a matching birthday in their group.')
    print('Thats probably more than you would think!\n')
        

def main():
    # get a valid number of birthdays to be generated
    no_bds = -1
    while True:
        no_bds = int(input('How many birthdays shall i generate? (Max=100)\n>'))
        if (0 < no_bds <=100):
            break
        else:
            print('please enter a valid number')

    # generate 1 simulation and display it
    run_1_simulation(no_bds)

    # generate 100,000 simulations of it
    print(f'\nGenerating {no_bds} random birthdays 100,000 times...\n')
    run_100k_simulations(no_bds)


if __name__ == '__main__':
    main()