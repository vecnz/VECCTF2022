#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>


char user_input[22];
char first_flag[] = "AHOY{g3tt1ng_warm33rr}";
unsigned char xor_string[] = {4, 13, 10, 28, 62, 29, 117, 55, 55, 26, 39, 0, 0, 32, 26, 45, 117, 49, 49, 49, 49, 56};

char final_flag[] = {0, 0, 0, 0, 0, 23, 70, 65, 32, 40, 16, 116, 17, 86, 0, 55, 67, 69, 71, 71, 4, 0};

void give_flag(){

    char *p = malloc(23);
    memset(p, 0, 23);

    for (int i = 0; i < 22; i++)
    {
        p[i] = user_input[i] ^ final_flag[i];
    }
    printf("Flag: %s\n", p);
    
}

int main(int argc, char const *argv[])
{
    printf("Brrr, me a lil' bit cold from ye wellington weathe'\nHelp me warm up, will ye?\n");

    
    printf("Lets try and light me a fire ");

    
    scanf("%22c", user_input);
    getc(stdin);

    if (strcmp(user_input, first_flag))
    {
        printf("Blast me, me fingers have frozen off!\n");
        return -1;
    }
    printf("The fire be burning well, add me some logs will ye? ");
    scanf("%23c", user_input);

    
    for (int i = 0; i < 22; i++)
    {
        if( (unsigned) (user_input[i] ^ xor_string[i]) != 69){
            printf("Siver me timbers, how'd ye loose the logs?");
            return -1;
        };

    }

    printf("All o' this here fire, make me feel sleeby\n");
    printf("I will give ye the flag when I get up on deck\n");
    sleep(4294967295);
    give_flag();

    return 0;
}
