# stegnography_with_cryptography  | NoobMaster

- Description: stegnography meets cryptography

1.jpg:/attachments/stegnography_with_cryptography/1.jpg
2.jpg:/attachments/stegnography_with_cryptography/2.jpg

# Write up
There are 2 parts, stegnography and cryptography as mentioned in description
You are given 1.jpg and 2.jpg, run stegseek(stegseek tool is used to bruteforce the hidden data from steghide using the wordlist provided)with rockyou.txt on both files.
`stegseek 1.jpg /usr/share/wordlists/rockyou.txt`
`stegseek 2.jpg /usr/share/wordlists/rockyou.txt`
now stegnography part ends and cryptography part begins - 
a.txt is - `0xdeadbeef`
b.txt is - `^HT\x07\x1b\x1f\x11\x11V\x01^H\x03\x17U\x14\n\x1c:\x11\x01\x0c\x0c:\x02\x16\x1b\x15\x11VW\nP\x15\t\x1d=T\x169V\r\nD\x1c`

now we xor them - 
b.txt doesnt work when we open it so we put it as bytes
```py
from pwn import *
key = open('a.txt').read()
enc_flag = b'^HT\x07\x1b\x1f\x11\x11V\x01^H\x03\x17U\x14\n\x1c:\x11\x01\x0c\x0c:\x02\x16\x1b\x15\x11VW\nP\x15\t\x1d=T\x169V\r\nD\x1c'
print(xor(key,enc_flag)) 
```
# Flag - n00bz{st3gn0gr4phy_w1th_crypt0gr4phy_1s_fun!}
