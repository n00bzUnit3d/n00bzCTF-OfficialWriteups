#!/usr/bin/env python3
#
# Polymero
#

# Imports
from pwn import *

# Connection
host = "0.0.0.0"
port = 5000

s = remote(host, port)

#context.log_level = "debug"

s.recvuntil(b"N: ")
N = int(s.recvuntil(b"\n", drop=True).decode())

s.recv()
s.sendline(b"1")
s.recvuntil(b"| ")
ENC = int(s.recvuntil(b"\n", drop=True).decode())

def play(x):
    s.recv()
    s.sendline(b"p")
    s.recv()
    s.sendline(str(x).encode())
    s.recvuntil(b"|  ")
    return s.recvuntil(b"\n", drop=True).decode()

c = ENC
b = ENC
play(c)

res = ''
for k in range(1024 - 32):

    print(len(res), end='\r', flush=True)
    
    b = pow(b, 2, N * N)
    c = (c * b) % (N * N)
    ret = play(c)

    if ret[0] == 'W':
        res = '1' + res
    elif ret[0] == 'C':
        res = '0' + res
    else:
        print('Oh oh')
    
print( ((int(res, 2) << 1) ^ 1).to_bytes(128, 'big').lstrip(b"\x00") )