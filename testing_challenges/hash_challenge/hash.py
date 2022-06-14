#!/usr/bin/env python3
import hashlib
try:
    with open('./flag.txt') as f:
        flag = f.read()
except FileNotFoundError:
    print("Error flag file not found, Contact administrator")
    exit(-1)

user_string = '''Hash
[F]lag
[I]nput
[E]xit
'''

def check_flag_hash():
    while (1):
        try:
            first_index = int(input('Start: '))
            second_index = int(input('End: '))
        except ValueError:
            print('Need an actual number')
            continue

        start = min(first_index, second_index)
        end = max(second_index, second_index)

        if end - start < 3:
            print('Need a larger gap')
            continue

        flag_part = flag[start:end]

        m = hashlib.sha512()
        m.update(flag_part.encode())
        flag_hash = m.digest()
        
        print('Your hash: ' + flag_hash.hex())
        break

def hash_user_input():
    user_input = input('Enter input to be hashed: ')
    m = hashlib.sha512()
    m.update(user_input.encode())
    hash = m.digest()
    print('Your hash: ' + hash.hex())

while (1):
    user_input = input(user_string)

    if user_input == 'f':
        check_flag_hash()
    elif user_input == 'i':
        hash_user_input()
    elif user_input == 'e':
        exit()

