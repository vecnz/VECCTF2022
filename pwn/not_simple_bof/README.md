# Not Simple BoF

## Description 
We had a simple BOF, now we have a not simple bof

**Category: pwn** 

**Difficulty: medium**

**Author: Ava (sSt3lla#8011)** 

**Flag: AHOY{N0t_S0_s1mpl3}**


## Exploit
There are two gets functions, the first one is unexploitable, as you will not be able to overflow anything useful\
For the second gets, it seems like it is not exploitable, \
however you can overflow the main function return to the win function and win