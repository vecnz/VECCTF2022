#include <stdio.h>
#include <stdlib.h>

void win(){
    FILE* f;
    char flag[64];
    
    f = fopen("flag.txt", "r");
    if (!f)
    {
        printf("Error reading flag\n");
        exit(-1);
    }
    fread(flag, 1, 64, f);
    printf("Flag: %s\n", flag);
    fflush(stdin);
    fclose(f);
}

void overflow_me(){
    char buf[32];
    puts("What be the pirate code: ");
    gets(buf);
    printf("Ye gave: ");
    puts(buf);

    unsigned int ret_addr = (unsigned int)__builtin_return_address(0);
    printf("We be goin' aft to: %p\n", ret_addr);

    if (__builtin_return_address(0) != 0x401397)
    {
        printf("Yaaaaah, the stack has been smashed!");
        exit(-1);
    } 
}

char name[32];

int main(int argc, char const *argv[])
{
    setvbuf(stdout, NULL, _IONBF, 0);
    setvbuf(stdin, NULL, _IONBF, 0);
    setvbuf(stderr, NULL, _IONBF, 0);

    printf("What be yer gentleman o' fortune name? ");
    gets(name);

    overflow_me();
    return 0;
}
