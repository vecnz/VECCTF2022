#!/usr/bin/env python3
import secrets, hashlib, sys

class Pow():

    def __init__(self, suffix_size, difficulty, zeros=[b'0']):
        self.difficulty = difficulty
        self.suffix_size = suffix_size
        self.zeros = zeros
    
    def create_challenge(self):
        self.hash = secrets.token_hex(self.suffix_size)
        self.end_char = secrets.choice(self.hash) 
        self.chall = self.end_char * self.difficulty

    def check_solution(self, suffix):
        hash_bytes = bytes.fromhex(self.hash + suffix)
        full_hash = hashlib.sha256(hash_bytes).digest()
        chall_bytes = bytes.fromhex(self.chall)
        return full_hash.endswith(chall_bytes)

for i in range(2, 8, 2):
    user_challenge = Pow(32, i, secrets.token_hex().encode())
    user_challenge.create_challenge()

    print(f"Arrh, solve me challenge such that sha256({user_challenge.hash} + suffix) ends with {user_challenge.chall}")
    user_suffix = input("Your suffix: ")

    if len(user_suffix) % 2 != 0:
        print("suffix must contain an even amount of characters")
        exit(1)

    if not user_challenge.check_solution(user_suffix):
        print('Wrong suffix')
        sys.exit(0)

    print('Correct suffix')

print('Ye merry lass, here is the flag:')
with open('flag.txt', 'r') as f:
    print(f.read())
