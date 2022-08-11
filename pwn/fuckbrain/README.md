# Fuckbrain

Yaar, the code, my brain, its, its, its been fuckbrained!


## Description 
**Category: pwn** 

**Difficulty: hard (I think)**

**Author: Ava (sS3tlla#8011)** 

**Flag: AHOY{1_Gadg3t_1__Sh0t}**

## Exploit

There is a lack of bounds checking on the compiled code.\
This allows us to directly edit the return address of the main function.\
Exploitation wise, there are many routes possible, but they all will require a info leak to begin with.
\
\
Personally I found that the most efficent way possible, was to leak the return address, since this returns to libc (or like main libc or something), so we directly have a libc leak.\
From here we utilise a one gadget and then we cat the flag.
\ 
\

x.py is llike rly short in terms of exploitation, but we basically move the like pointer to the return address, \
leak it, move it back, and overwrite it with a one gadget