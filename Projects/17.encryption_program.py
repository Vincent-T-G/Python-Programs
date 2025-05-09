#This is python project number 17
#TITLE:ENCRYPTION PROGRAM

#It's a substitution cypher encryption program using python

import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters

chars = list(chars)

key = chars.copy()

random.shuffle(key)


#Encryption

plain_text = input("Enter the message to be encrypted: ")
cypher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cypher_text += key[index]

print(f"Your message: {plain_text}")
print()
print(f"The encrypted message: {cypher_text}")

#Decryption

cypher_text_text = input("Enter the message to be decrypted: ")
plain_text = ""

for letter in cypher_text_text:
    index = key.index(letter)
    plain_text += chars[index]

print(f"The encrypted message: {cypher_text}")
print()
print(f"Your original message: {plain_text}")