#ifndef VM_H
#define VM_H

typedef struct simple_vm
{
    char stack[256];
    int sp;
    char instructions[1024];
    int ip;
    int running;

} *SIMPLE_VM;

SIMPLE_VM init_vm(char *instructions);
void destroy_vm(SIMPLE_VM simple_vm);
void step(SIMPLE_VM simple_vm);

#endif