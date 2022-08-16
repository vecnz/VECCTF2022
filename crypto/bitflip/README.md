# Bitflip

## Description 
CBC encryption is very secure so we have used it to make sure no pirates can break the encryption

**Category: crypto** 

**Difficulty: medium**

**Author: Darkflame72** 

**Flag: AHOY{d0nt_u5e_C8C}**


## Exploit
We are provided with the original text and the encrypted text. The first 16 bytes of the encrypted message is the IV and the last 16 is the text. With CBC every block is XORed with the previous block with the first block using the IV. We can bitflip the char (pos 8) in the first block which will change a 0 to a 1. This will then cause the next block to be flipped to a 1