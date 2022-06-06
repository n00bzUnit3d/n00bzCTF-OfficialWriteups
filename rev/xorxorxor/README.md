# xorxorxor | NoobHacker

- Description: xor ftw

xorxorxor:/attachments/xorxorxor/xorxorxor

# Write up

Added by noobmaster, script to solve - 
```c
#include <stdio.h>
void main() {
	char input[24] = "n12a~~~7zV;xSyf<Os!``4k";
	for (int i = 0; i < 23; i++) {
        input[i] = input[i] ^ i;
		printf("%s\n", input);
    }
}
```

Result - 
```n12a~~~7zV;xSyf<Os!``4k
n02a~~~7zV;xSyf<Os!``4k
n00a~~~7zV;xSyf<Os!``4k
n00b~~~7zV;xSyf<Os!``4k
n00bz~~7zV;xSyf<Os!``4k
n00bz{~7zV;xSyf<Os!``4k
n00bz{x7zV;xSyf<Os!``4k
n00bz{x0zV;xSyf<Os!``4k
n00bz{x0rV;xSyf<Os!``4k
n00bz{x0r_;xSyf<Os!``4k
n00bz{x0r_1xSyf<Os!``4k
n00bz{x0r_1sSyf<Os!``4k
n00bz{x0r_1s_yf<Os!``4k
n00bz{x0r_1s_tf<Os!``4k
n00bz{x0r_1s_th<Os!``4k
n00bz{x0r_1s_th3Os!``4k
n00bz{x0r_1s_th3_s!``4k
n00bz{x0r_1s_th3_b!``4k
n00bz{x0r_1s_th3_b3``4k
n00bz{x0r_1s_th3_b3s`4k
n00bz{x0r_1s_th3_b3st4k
n00bz{x0r_1s_th3_b3st!k
n00bz{x0r_1s_th3_b3st!}```

# Flag - n00bz{x0r_1s_th3_b3st!}
