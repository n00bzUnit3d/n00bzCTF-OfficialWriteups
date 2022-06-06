#include <stdio.h>
#include <string.h>

// n00bz{x0r_1s_th3_b3st!}

int main(int argc, char** argv) {
    char input[23];
    printf("Give me the flag: ");
    scanf("%23s", input);
    for (int i = 0; i < 23; i++) {
        input[i] = input[i] ^ i;
    }
    if (strcmp(input, "n12a~~~7zV;xSyf<Os!``4k") == 0) {
        puts("Correct!");
    }
    else {
        puts("Wrong!");
    }

    return 0;
}
