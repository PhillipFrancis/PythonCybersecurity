#!/usr/bin/env python3
# Script that encrypts/decrypts text using ROT13
# By Phillip Francis 2/2/24

# Asking for message
Source_Message = input('What is your message?: ')
# Change message to lower case
Source_Message = Source_Message.lower()
Final_message = ''
# loop through each letter
for letter in Source_Message:
    # Convert letter to number
    ascii_number = ord(letter)
    # check if letter is between A - Z
    if ascii_number >= 97 and ascii_number <= 122:
        # Add 13 to number if a letter
        ascii_number += 13
        # check if it is still a letter. If not, subtract 26
        if ascii_number >= 122:
            ascii_number -= 26
    Final_message = Final_message + chr(ascii_number)
# Print out message
print(Final_message)