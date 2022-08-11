#include <stdio.h>
#include "vm.h"

char a[] = "It was a bad idea\nCalling you up";

char instructions[] = {
1, 
 'Y',
 'a',
 'a',
 'a',
 'r',
 ',',
 ' ',
 't',
 'r',
 'y',
 ' ',
 'o',
 'u',
 't',
 ' ',
 'm',
 'e',
 ' ',
 's',
 'i',
 'm',
 'p',
 'l',
 'e',
 ' ',
 'v',
 'm',
 ',',
 ' ',
 'i',
 't',
 ' ',
 'b',
 'e',
 ' ',
 's',
 'm',
 'a',
 'l',
 'l',
 ',',
 ' ',
 'b',
 'u',
 't',
 ' ',
 'i',
 't',
 ' ',
 'b',
 'e',
 ' ',
 'w',
 'o',
 'r',
 'k',
 'i',
 'n',
 'g',
 '.',
 ' ',
 'S',
 'a',
 'v',
 'v',
 'y',
 '?',
 '\n',
 '\00',

/*Print*/
0, 69,
0, 1,
0xFF,

/*Push Zero*/
0, 0,

/*Cmp to 8*/
0, 8,
0x20,

/*jmp if equal not calcualted yet*/
'\x30', 18,

/*Sleep for 0 second*/
0, 1,
0, 2,
0xFF,

/* Push the thingy*/
1,
'.',
' ',
'\00',

/*Hopefully print it*/
0, 3,
0, 1,
0xFF,

/*Increment the top*/
0x10,

//Jump up
0x31, 235,

/*Print a newline*/
1,
'\n',
'\00',


/**/
0, 2,
0, 1,
0xFF,

/*Pop the stack cos we don'e need to top value anymore*/
2,

/*Print getting input*/
1,
 'W',
 'h',
 'a',
 't',
 ' ',
 'b',
 'e',
 ' ',
 't',
 'h',
 'e',
 ' ',
 'f',
 'l',
 'a',
 'g',
 ' ',
 'f',
 'o',
 'r',
 ' ',
 't',
 'h',
 'i',
 's',
 ' ',
 's',
 'h',
 'i',
 'p',
 '?',
 ' ',
 '\00',

0, 33,
0, 1,
0xFF,

/*Read 22 bytes of input*/
0, 22,
0, 0,
0xFF,



/*Extremly long comparison*/

/*Push*/
0, '}',
/*cmp*/
0x20,
/*jne*/
0x32, 64,
2,
    
/*Push*/
0, 'D',
/*cmp*/
0x20,
/*jne*/
0x32, 58,
2,
    
/*Push*/
0, '0',
/*cmp*/
0x20,
/*jne*/
0x32, 52,
2,
    
/*Push*/
0, 'o',
/*cmp*/
0x20,
/*jne*/
0x32, 46,
2,
    
/*Push*/
0, '0',
/*cmp*/
0x20,
/*jne*/
0x32, 40,
2,
    
/*Push*/
0, 'g',
/*cmp*/
0x20,
/*jne*/
0x32, 34,
2,
    
/*Push*/
0, '_',
/*cmp*/
0x20,
/*jne*/
0x32, 28,
2,
    
/*Push*/
0, '3',
/*cmp*/
0x20,
/*jne*/
0x32, 22,
2,
    
/*Push*/
0, 'B',
/*cmp*/
0x20,
/*jne*/
0x32, 16,
2,
    
/*Push*/
0, '_',
/*cmp*/
0x20,
/*jne*/
0x32, 10,
2,
    
/*Push*/
0, 'Y',
/*cmp*/
0x20,
/*jne*/
0x32, 4,
2,
    
/*jmp across this jmp to get back onto the if statements*/
0x31, 3,

/*Jmp down to the next jump so we can print that its wrong*/
0x31, 69,


/*Push*/
0, 'e',
/*cmp*/
0x20,
/*jne*/
0x32, 64,
2,
    
/*Push*/
0, '6',
/*cmp*/
0x20,
/*jne*/
0x32, 58,
2,
    
/*Push*/
0, 't',
/*cmp*/
0x20,
/*jne*/
0x32, 52,
2,
    
/*Push*/
0, '_',
/*cmp*/
0x20,
/*jne*/
0x32, 46,
2,
    
/*Push*/
0, 'm',
/*cmp*/
0x20,
/*jne*/
0x32, 40,
2,
    
/*Push*/
0, 'V',
/*cmp*/
0x20,
/*jne*/
0x32, 34,
2,
    
/*Push*/
0, '{',
/*cmp*/
0x20,
/*jne*/
0x32, 28,
2,
    
/*Push*/
0, 'Y',
/*cmp*/
0x20,
/*jne*/
0x32, 22,
2,
    
/*Push*/
0, 'O',
/*cmp*/
0x20,
/*jne*/
0x32, 16,
2,
    
/*Push*/
0, 'H',
/*cmp*/
0x20,
/*jne*/
0x32, 10,
2,
    
/*Push*/
0, 'A',
/*cmp*/
0x20,
/*jne*/
0x32, 4,
2,

/*Jump accross this jump*/
0x31, 3,

/*Jump accross the error msg*/
0x31, 54,

1, 
 'B',
 'l',
 'i',
 'm',
 'e',
 'y',
 '!',
 ' ',
 'Y',
 'e',
 ' ',
 'm',
 'a',
 'n',
 'a',
 'g',
 'e',
 'd',
 ' ',
 't',
 'o',
 ' ',
 'f',
 'i',
 'n',
 'd',
 ' ',
 'y',
 'e',
 ' ',
 'a',
 ' ',
 'c',
 'o',
 'r',
 'r',
 'e',
 'c',
 't',
 ' ',
 'f',
 'l',
 'a',
 'g',
 '\n',
 '\00',

/*Print and halt*/
0, 46,
0, 1,
0xFF,
0xCC,

1,
'A',
 'v',
 'a',
 's',
 't',
 ' ',
 'Y',
 'e',
 ',',
 ' ',
 't',
 'h',
 'a',
 't',
 ' ',
 'b',
 'e',
 ' ',
 'n',
 'o',
 't',
 ' ',
 't',
 'h',
 'e',
 ' ',
 'f',
 'l',
 'a',
 'g',
 '!',
 '\n',
 '\00',

/*Print and halt*/
0, 33,
0, 1,
0xFF,
0xCC,

};

int main(){

    setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stdin, NULL, _IONBF, 0);
	setvbuf(stderr, NULL, _IONBF, 0);

    SIMPLE_VM simple_vm = init_vm(instructions);
    while (simple_vm->running)
    {
        step(simple_vm);
    }
}