#!/usr/bin/env python3
import secrets, hashlib, sys

class Pow():

    def __init__(self, prefix_size, difficulty, zeros=[b'0']):
        self.difficulty = difficulty
        self.prefix_size = prefix_size
        self.zeros = zeros
    
    def create_challenge(self):
        self.hash = secrets.token_hex(self.prefix_size)
        self.end_char = secrets.choice(self.hash) 
        self.chall = self.end_char * self.difficulty

    def check_solution(self, prefix):
        hash_bytes = bytes.fromhex(self.hash + prefix)
        full_hash = hashlib.sha256(hash_bytes).digest()
        chall_bytes = bytes.fromhex(self.chall)
        return full_hash.endswith(chall_bytes)

for i in range(2, 10, 2):
    user_challenge = Pow(32, i, secrets.token_hex().encode())
    user_challenge.create_challenge()

    print(f"Arrh, solve me challenge such that sha256({user_challenge.hash} + prefix) ends with {user_challenge.chall}")
    user_prefix = input("Your prefix: ")

    if len(user_prefix) % 2 != 0:
        print("Prefix must contain an even amount of characters")
        exit(1)

    if not user_challenge.check_solution(user_prefix):
        print('Wrong prefix')
        sys.exit(0)

    print('Correct prefix')

print('Ye merry lass, here is the flag:')
with open('flag.txt', 'r') as f:
    print(f.read())