alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#Functions
def encrypt(plain_text, shift_amount):
    encoded =''
    for letter in plain_text:                                        #Verify each letter passed in the text
        indexed_letter = alphabet.index(letter)+shift_amount         #Create a new index to replace the letter
        if indexed_letter > alphabet.index('z'):                     #If the new index is greather than 'z' index, the difference will be the shift to go through the alphabet again.
            indexed_letter -= alphabet.index('z')+1
            encoded += alphabet[indexed_letter]                      #replace the letter
        else:
            encoded +=alphabet[indexed_letter]                       #Replace the letter
    return encoded


def decrypt(plain_text, shift_amount):
    decoded =''
    for letter in plain_text:                                        #Verify each letter passed in the text
        indexed_letter = alphabet.index(letter)-shift_amount         #Create a new index to replace the letter
        if indexed_letter < alphabet.index('a'):                     #If the new index is lesser than 'a' index, the difference will be the shift to go through reversely the alphabet.
            indexed_letter = alphabet.index('z')+1 + indexed_letter
            decoded += alphabet[indexed_letter]                      #replace the letter
        else:
            decoded +=alphabet[indexed_letter]                       #Replace the letter
    return decoded