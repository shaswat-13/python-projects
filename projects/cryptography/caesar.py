# program to generate a cyphered text

import pyperclip # used to copy text to the clipboard

letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'

# choose either to encrypt or decrypt
def get_task():
    while True:
        print('\nDo you want to (e)ncrypt or (d)ecrypt? ')
        resp = input('> ')
        if resp.lower() == 'e' or resp.lower() == 'd':
            return resp.lower()
        print('Please enter valid letter (e or d)')

# get the code number to encrypt the message
def get_valid_code():
    print('\nPlease choose a code (1-25)')
    resp = input('> ')
    if resp.isdigit():
        if (1 <= int(resp) <= 25):
            return int(resp)
    print('Please enter valid code')   

# encrypt the message
def encrypt(code, txt):
    enc_msg = str()
    for letter in txt:
        if letter == ' ':
            enc_msg = enc_msg + ' '
        else:
            index = letters.index(letter)
            index += code
            index = index % 26
            enc_msg = enc_msg + letters[index]
    print('The encrypted message is: ')
    print(enc_msg)
    pyperclip.copy(enc_msg)
    print('Encrypted message copied to clipboard')

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
    print('The decrypted message is: ')
    print(dec_msg)
    pyperclip.copy(dec_msg)
    print('Decrypted message copied to clipboard')

def main():
    task = get_task()
    print('\nPlease enter the message: ')
    msg = input('> ').upper()
    code = get_valid_code()
    if task == 'e':
        encrypt(code, msg)
    
    elif task == 'd':
        decrypt(code, msg)

if __name__ == '__main__':
    main()

    

