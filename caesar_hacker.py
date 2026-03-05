# program to decipher the caesar code

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# decrypt the message
def decrypt(code, txt):
    dec_msg = str()
    for letter in txt:
        if letter == ' ':
            dec_msg = dec_msg + ' '
        else:
            index = letters.index(letter)
            index -= code
            index = index % 26
            dec_msg = dec_msg + letters[index]  
    print(f'Code {code}: {dec_msg}')

def main():
    print('\nPlease enter the message: ')
    msg = input('> ').upper()

    for num in range(1,25):
        decrypt(num, msg)

if __name__ == '__main__':
    main()

    

