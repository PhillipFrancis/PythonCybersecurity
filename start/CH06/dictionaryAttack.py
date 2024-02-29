#!/usr/bin/env python3
# Script that performs a dictionary attack against known password hashes
# Needs a dictionary file, suggested to use https://github.com/danielmiessler/SecLists/tree/master/Passwords/Common-Credentials
# By Phillip Francis 2/6/2024

# import modules
import os
import crypt

# Function to test passwords
def test_password(Algor_salt, hashed_password, Pass_Guess):
    #Use the algorsalt to hash the guess
    Hashed_guess = crypt.crypt(Pass_Guess, Algor_salt)
    #Compare salted guess against hashed password
    if Hashed_guess == hashed_password:
        return True
    return False

# load a dictionary file
dir_path = os.path.dirname(os.path.realpath(__file__))
f = open(dir_path + "/top10.txt", "r")
passwords = f.readlines()
f.close

# Prompt user for Algorithm and salt
Algor_salt = input('what is the algorithm and salt: ')
# Prompt User for salted hash
Hashed_password = input('what is the full hashed password: ')

# loop through each password 
for password in passwords:
    password = password.strip
    result = test_password(Algor_salt, Hashed_password, password):
    if result:
        print('Match Found: {0}'.format(password))
        break
