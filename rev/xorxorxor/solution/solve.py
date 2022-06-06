#!/usr/bin/env python3
flag = b'n12a~~~7zV;xSyf<Os!``4k'

for i in range(len(flag)):
    print(chr(flag[i] ^ i), end='')

print()
