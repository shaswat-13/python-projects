# a program to see the collatz sequence

def main():
    print('Enter any number ')
    num = int(input('> '))

    while True:
        # if number is 1 then end
        if num == 1:
            print('1.')
            break
        # display each number 
        print(f'{num}, ', end='')
        
        # if number is even then new number is half of it
        if num % 2 == 0:
            num = int(num / 2)
        
        # if number is odd then new number is 3n+1
        elif num % 2 != 0:
            num = 3 * num + 1

if __name__ == '__main__':
    main()