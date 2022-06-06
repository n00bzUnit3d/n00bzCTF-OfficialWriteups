from pwn import xor
known_plaintext = b'n00bz{p'
enc = b'_\x03\x03U\x11\x1e\t]\x07J\x06\x05\x02&F\x02G_4\x1dICl^\x07\x19V&]\x02X\x044\x15\x15\x05J\x02Y\x0c:\x0e\x00G[h\rT\x0b\x02N'
full_key = xor(known_plaintext,enc)[:7]
flag = xor(full_key,enc)
print(flag)
