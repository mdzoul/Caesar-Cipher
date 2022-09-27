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
    print(f"The {direction}d text is {end_text}.")
    # Allows user to restart program
    input()

while True:
    clear()
    logo()
    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: ")
    clear()
    logo()
    text = input("Type your message: ").lower()
    clear()
    logo()
    text_list = [*text]
    shift = int(input("Type the shift number: "))
    clear()
    logo()
    
    # If the user enters a shift that is greater than the number of letters in the alphabet
    if shift > 26:
        shift = shift % 26
    
    caesar()