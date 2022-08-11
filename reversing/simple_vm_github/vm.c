#include <string.h>
#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include "vm.h"


SIMPLE_VM init_vm(char *instructions){
    SIMPLE_VM simple_vm = malloc(sizeof(struct simple_vm));

    memset(simple_vm->instructions, 0, 1024);
    memset(simple_vm->stack, 0, 256);

    simple_vm->sp = 0;
    simple_vm->running = 1;
    memcpy(simple_vm->instructions, instructions, 1024);

    return simple_vm;
}

void push(SIMPLE_VM state, char val){
    state->stack[state->sp++] = val;
    //state->sp++;
    
}

char pop(SIMPLE_VM state){
    char ret = state->stack[--state->sp];
    return ret;
}

void step(SIMPLE_VM state){

    char instruction = state->instructions[state->ip];

    //halt
    if (instruction == '\xCC')
    {
        state->running = 0;
    }

    //Syscall
    else if (instruction == '\xFF')
    {
        char syscall = pop(state);
        char amount = pop(state);

        //Reading
        if (syscall == 0)
        {
            read(0, state->stack + state->sp, amount);
            state->sp += amount;
        }
        else if (syscall == 1)
        {   
            write(1, state->stack + state->sp - amount, amount);
            state->sp -= amount;
        }
        else if (syscall == 2)
        {
            sleep(amount);

        }
        
    }

    //push string
    else if (instruction == '\x01')
    {

        while (1)
        {

            char str = state->instructions[++state->ip];

            //printf("Str is %d\n", str);
            push(state, str);
            if (str == 0)
            {
                break;
            }
            
        }
        
    }

    //push number
    else if (instruction == '\x00')
    {
       char num = state->instructions[++state->ip];
       push(state, num);
    }

    //pop
    else if (instruction == '\x02')
    {
       pop(state);
    }

    //Inc the top
    else if (instruction == '\x10')
    {
       char num = pop(state);
       num++;
       push(state, num);
    }
    

    //cmp
    else if (instruction == '\x20')
    {
        char f1 = pop(state);
        char f2 = pop(state);
        push(state, f2);

        if (f1 == f2)
        {
            push(state, 1);
        }
        else {
            push(state, 0);
        }
        
    }


    //jmp
    else if (instruction == '\x31')
    {
        char jmp_amount = state->instructions[++state->ip];
        state->ip += jmp_amount;
        state->ip--;
    }
    

    //je
    else if (instruction == '\x30')
    {
        char top = pop(state);
        char jmp_amount = state->instructions[++state->ip];
        if (top == 1)
        {
            state->ip += jmp_amount;
            state->ip--;
        }
        
    }

    //jne
    else if (instruction == '\x32')
    {
        char top = pop(state);
        char jmp_amount = state->instructions[++state->ip];
        if (top != 1)
        {
            state->ip += jmp_amount;
            state->ip--;
        }
        
    }

    else{
        printf("Invalid instruction (%x)\n", (unsigned char) instruction);
        state->running = 0;
    }
    
    state->ip++;
}