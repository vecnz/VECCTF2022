#!/usr/bin/env python3
import secrets, hashlib

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
