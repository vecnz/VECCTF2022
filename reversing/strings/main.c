#include <stdio.h>
#include <string.h>

char* flag = "A\0H\0O\0Y\0{\0b\0e\0t\0t\0e\0r\0_\0s\0t\0r\0i\0n\0g\0_\0s\0t\0o\0r\0a\0g\0e\0}";

int main(int argc, char* argv[]) {
    printf("Arr' what is the flag?\n");

    if (argc != 2 || strlen(argv[1]) != 27) {
        printf("I must of hidden it from that dastardly strings command\n");
        return 0;
    }

    for (int i = 0; i < strlen(argv[1]); i++) {
        if (argv[1][i] != flag[i * 2]) {
            printf("I must of hidden it from that dastardly strings command\n");
            return 0;
        }
    }

    printf("You got the flag!\n");

    return 0;
}