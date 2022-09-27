# Caesar Cipher v1
from alphabet import letters
from replit import clear

while True:
    clear()
    
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    text_list = [*text]
    shift = int(input("Type the shift number:\n"))
    
    def encrypt():
        # Shift each letter of the 'text' *forwards* in the alphabet by the shift amount
        shift_forward = letters[shift:] + letters[:shift]
        
        encoded_text = ""
        for char in text:
            index = letters.index(char)
            encoded_text += shift_forward[index]
        # Print the encrypted text.
        print(f"The encoded text is {encoded_text}")
    
    def decrypt():
        # Shift each letter of the 'text' *backwards* in the alphabet by the shift amount
        shift_backward = letters[-shift:] + letters[:-shift]
    
        decoded_text = ""
        for char in text:
            index = letters.index(char)
            decoded_text += shift_backward[index]
        # Print the decrypted text.
        print(f"The decoded text is {decoded_text}")
    
    if direction == "encode":
        encrypt()
        input()
    if direction == "decode":
        decrypt()
        input()