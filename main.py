# Caesar Cipher v2
from letnumsym import *
from replit import clear
from ascii_art import *

def caesar():
    # Shift each letter of the 'text' in the alphabet by the shift amount
    if direction == "encode":
        shift_letters = letters[shift:] + letters[:shift]
    elif direction == "decode":
        shift_letters = letters[-shift:] + letters[:-shift]

    end_text = ""
    for char in text:
        # Make code run even if user enters number/symbol/space
        if char in letters:
            index = letters.index(char)
            end_text += shift_letters[index]
        elif char in num_sym:
            end_text += char
        
    # Print the end text
    print(f"The \33[1m{direction}d\33[0m message is:\n\33[31m{end_text}\33[0m")

should_cont = True
while should_cont == True:
    clear()
    logo()

    print("\33[32m---Starting Cipher---\33[0m\n")
    
    direction = input("Type \33[1m[Encode]\33[0m to encrypt\nType \33[1m[Decode]\33[0m to decrypt\n").lower()
    clear()
    logo()
    text = input("Type the message:\n").lower()
    clear()
    logo()
    text_list = [*text]
    shift = int(input("Code number: "))
    clear()
    logo()
    
    # If the user enters a shift that is greater than the number of letters in the alphabet
    if shift > 26:
        shift = shift % 26
    
    caesar()
    # Allows user to restart program
    cont = input("\33[1m\nContinue?\33[0m Y/N\n")
    if cont == "y":
        should_cont = True
    elif cont == "n":
        should_cont = False
        clear()
        logo()
        print("\33[31m---Shutting Down---\33[0m")