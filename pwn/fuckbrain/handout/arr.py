import string, tempfile, os, subprocess, shutil, sys

def compile_brain_fuck(brain_code):
    replace_dict = {
        '@':'++p;',
        'r':'--p;',
        'R':'++*p;',
        '*':'--*p;',
        'u':'putchar(*p);',
        '(':'*p=getchar();',
        'k':'while(*p){',
        'K':'}'
    }
    optimising_dict = {
        '@':'p+={};',
        'r':'p-={};',
        'R':'*p+={};',
        '*':'*p-={};',
    }
    code = []

    #Digits that have been collected
    digit_list = []
    for char in brain_code:

        if char in string.hexdigits:
            digit_list.append(char)

        elif char in replace_dict:
            #Turns into a string
            collected_num = ''.join(digit_list)
            
            if collected_num == '':
                collected_num = 1
            else:
                #Turns into a int
                collected_num = int(collected_num, 16)

            #Reset digit list
            digit_list = []

            if char in optimising_dict and collected_num != 1:
                emitted_code = optimising_dict[char].format(collected_num)
            else:
                emitted_code = collected_num * replace_dict[char]
                
            #print(emitted_code)
            code.append(emitted_code)
    #Return as string
    return '\n'.join(code)


#compile_code = compile_brain_fuck(brain_code)

def run_code(compiled_code):

    c_code = '''
#include <stdio.h>
#include <signal.h>
#include <stdlib.h>
#include <unistd.h>

void limit_time(int sig) {
  if (sig == SIGALRM) {
  	printf("Yaa, this ship has sailed away!");
    exit(0);
  }
}

int main(){
    setvbuf(stdout, NULL, _IONBF, 0);
	setvbuf(stdin, NULL, _IONBF, 0);
	setvbuf(stderr, NULL, _IONBF, 0);

    signal(SIGALRM, limit_time);
	alarm(10);

    char a[1337] = {0}; char *p = a;
''' + compiled_code + '''
return 0;
}
'''

    with tempfile.TemporaryDirectory() as tmpdir:
        file_name = 'pirate.c'
        file_output = 'pirate'
        pirate_path = os.path.join(tmpdir, file_name)
        output_path = os.path.join(tmpdir, file_output)

        with open(pirate_path, 'w+') as f:
            f.write(c_code)

        gcc_path = shutil.which('gcc')
        if gcc_path is None:
            sys.exit('gcc not found')

        first_command = f'gcc {pirate_path} -o {output_path} -fpie -fstack-protector-all -z now'.split()
        subprocess.run(first_command)
        subprocess.run(output_path)
        

def main():
    user_input = input('Yarr be, enter me ye ship: ')
    compiled_code = compile_brain_fuck(user_input)
    run_code(compiled_code)
    print('Goodbye ye')
    
if __name__ == "__main__":
    main()
