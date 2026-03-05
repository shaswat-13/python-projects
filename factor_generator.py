import sys
import math

def get_response():
    while True:
        print('Enter any positive whole number (or Q to quit): ')
        resp = input('> ')
        if resp.upper() == 'Q':
            sys.exit()
        elif resp.isdigit():
            if int(resp) > 0:
                return int(resp)
        print('Enter a valid number')

def find_factors(n):
    factors = list()
    factors.append(1)
    if n != 1:
        factors.append(n)
    max = math.ceil(n/2)
    print(max)
    for i in range (2, max+1):
        if (n % i == 0):
            factors.append(i)

    factors.sort()
    print(f'The factors of {n} are: ')
    print(factors)

def main():
    num = get_response()
    find_factors(num)



if __name__ == '__main__':
    main()