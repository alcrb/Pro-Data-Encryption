#!/usr/bin/python

# ----------------------------- MODULES ------------------------------------------

from hashlib import sha256

# ----------------------------- COLORS ------------------------------------------

OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'


# ----------------------------- FUNCTIONS ------------------------------------------

def encrypt_file():

    input_file = input("File Name or Path File you need to Encrypt : ")
    output_file = input("Final File Name (.key),(.enc) : ")
    key = input("Password : ")
    print(f'{WARNING}Encrypting ...{ENDC}')
    keys = sha256(key.encode('utf-8')).digest()
    with open(input_file, 'rb') as f_input_file:
        with open(output_file, 'wb') as f_output_file:
            i = 0
            while f_input_file.peek():
                c = ord(f_input_file.read(1))
                j = i % len(keys)
                b = bytes([c ^ keys[j]])
                f_output_file.write(b)
                i = i + 1

    print(f'{OKGREEN}File Successfully Encrypted{ENDC}')

def decrypt_file():

    input_file = input("File Name or Path File you need to Decrypt : ")
    output_file = input("Final File Name : ")
    key = input("Password : ")
    print(f'{WARNING}Decrypting ...{ENDC}')
    keys = sha256(key.encode('utf-8')).digest()
    with open(input_file, 'rb') as f_input_file:
        with open(output_file, 'wb') as f_output_file:
            i = 0
            while f_input_file.peek():
                c = ord(f_input_file.read(1))
                j = i % len(keys)
                b = bytes([c ^ keys[j]])
                f_output_file.write(b)
                i = i + 1
    print(f'{OKGREEN}File Successfully Decrypted{ENDC}')
