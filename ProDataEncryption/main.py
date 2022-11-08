#!/usr/bin/python

# ----------------------------- MODULES ------------------------------------------

import time
from hashlib import sha256
from encryptfile import encrypt_file
from encryptfile import decrypt_file
from humanfriendly import format_timespan
from pyfiglet import Figlet

f = Figlet(font='slant')

# ----------------------------- COLORS ------------------------------------------

OKGREEN = '\033[92m'
WARNING = '\033[93m'
FAIL = '\033[91m'
ENDC = '\033[0m'

# ----------------------------- TITLE ------------------------------------------

print(f.renderText('Pro Data Encryption'))

print('Encrypt or Decrypt Files EASILY '
          '\n----------------------------------------------------------------------')
print('OPTIONS')

# ----------------------------- MAIN MENU ------------------------------------------

def main():
    number_int = 0

    while number_int == 0:
        number_int = 0
        number_str = input(f'1- Encrypt\n2- Decrypt\n3- Quit\n\nPlease choose a number : ')

        if number_str == '1':
            encrypt_file()
            break

        if number_str == '2':
            decrypt_file()
            break

        if number_str == '3':
            quit()
            break

        print(f'{FAIL}ERROR: Only number between 1 & 3 is accepted. Retry.{ENDC}')


number_min = 1
number_max = 3


if __name__ == '__main__':
    start = time.time()
    main()
    print(f'Execution time: {format_timespan(time.time() - start)}')


