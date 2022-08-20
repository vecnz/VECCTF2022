# Arrfox

## Description 
Yaar, this js engine looks OOB'y

**Category: pwn** 

**Difficulty: Extreme++**

**Author: Ava (sSt3lla#8011)** 

**Flag: AHOY{yAAr_YE_escaped_the_JS_eng1n3}**

## Exploit
Rough writeup \
So we ovewrite a arraybuffer getting arb r/w \
we then leak a random pointer that is adjacent to the .text section so we can leak two got entries \
one is system and the other is memmove \
