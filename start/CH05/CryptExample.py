#!/usr/bin/env python3
# Script that encrypts/decrypts text using cryptography module
# By 


# May need 'pip3 install cryptography' or
# 'pip3 install cryptography -U' prior to running
# Import necessary Python modules
from cryptography.fernet import Fernet

def create_key():
    # Generate an encryption key
    # Keep this key secret and store in a secure location
    key = Fernet.generate_key()
    print("Key:", key.decode())

def encrypt(plain_text, key):
    # Convert plain_text and key into bytes for encryption
    plain_text = plain_text.encode()
    key = key.encode()
    # Encrypt the data using the provided key
    cipher_text = Fernet(key).encrypt(plain_text)
    # Convert the cipher_text back to a string
    cipher_text = cipher_text.decode()
    return cipher_text

def decrypt(cipher_text, key):
    # Convert cipher_text and key into bytes
    cipher_text = cipher_text.encode()
    key = key.encode()
    # Decrypt the data using the provided key
    plain_text = Fernet(key).decrypt(cipher_text)
    # Convert plain_text back to a string
    plain_text = plain_text.decode()
    return plain_text