# Always Secure SSH

## Description 
Who are you? Where are you? It looks like you are trapped like the evil pirate you are, are you able to escape?


**Category: pwn** 

**Difficulty: medium**

**Author: Darkflame72** 

**Flag: AHOY{55h_15_50_53cur3}**

## Exploit
The server runs over a netcat connection which provides a basic shell. After looking around we follow the hint of `Who am I?` where we realise we are not the root user.

Navigating to the root directory we see there is a `.ssh` folder with keys. As the keys are not protected we can login to the root user using ssh.

`ssh -i /root/.ssh/id_rsa -o StrictHostKeyChecking=no root@localhost` this will present us with the key.
