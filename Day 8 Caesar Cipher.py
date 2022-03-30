#Imports
from Caesar_functions import encrypt, decrypt
from logo import logo

#Display
print(logo)

#Main Program
program_on = True
while program_on:
    while True:
        text = input("Type your message:\n").lower()
        if text.isalpha():  # Verify if only letters was entered.
            break
        else:
            print('Type only letters, please.')
    while True:
        try:
            shift = int(input("Type the shift number:\n"))  # verify if shift is numeric.
            break
        except:
            print('Only numbers are accepted here.')
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    if direction == 'encode':
        print(f'The encoded text is: {encrypt(text,shift)}')
    elif direction == 'decode':
        print(f'The decoded text is: {decrypt(text,shift)}')
    else:
        print('Please choose a valid answer.')
    while True:
        restart = input('Do you wanna do this again? [Y/N] ').upper()
        if restart == 'Y':
            print('Ok, here we go again.')
            break
        elif restart == 'N':
            print('See you later!')
            program_on = False
            break
        else:
            print('Please enter a valid answer.')
