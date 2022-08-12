#include <stdio.h>
#include <unistd.h>

__attribute__((constructor))
void setup() {
    setvbuf(stdout, 0, 2, 0);
    setvbuf(stdin, 0, 2, 0);
}

void pirates_control() {
    execve("/bin/sh", NULL, NULL);
}

void vuln() {
    char name[42];

    printf("What is the code to get the treasure: ");
    gets(name);
}

int main(void) {
    printf("Some rival pirates have stolen our treasure, they were muttering something about the secret to the universe or something. Can you get it back?\n");
    vuln();
    printf("The treasure has been lost to time, try again later\n");
}

treasure