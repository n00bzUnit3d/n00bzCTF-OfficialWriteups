from Crypto.Util.number import *
from pwn import xor
flag = b'n00bz{pREDACTED}'
key1 = b'REDACTED'
enc = b''
for i in range(len(flag)):
	enc += xor(key1[i],flag[i])
print(enc)
