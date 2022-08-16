#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pwn import *

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    return remote('localhost', 6666)

io = start()

io.recvuntil(b"Encrypted auth message: ")
hex = io.recvline().strip()

# take hex in as input and convert to bytes
in_bytes = bytearray.fromhex(hex.decode('utf-8'))

# bit flip element at index 8
in_bytes[8] ^= 1


io.sendline(bytes(in_bytes.hex(), 'utf-8'))

io.recvline()
flag = io.recvlineS()
log.info(flag)
io.close()
