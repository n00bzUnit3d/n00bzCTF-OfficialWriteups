from pwn import *
io = process('./chall')
chars = 'abcdefghijklmnopqrstuvwxyz1234567890{_}'
f = open('enc.txt').read()
f = f.replace('letter of flag ','').strip().replace('\n',' ')
#print(f.replace('  ',','))
enc_flag = []
flag = ''
enc_flag += f.split()
io.readline()
for j,i in enumerate(chars):
	
	#print(i)
	io.sendline(chars[j].encode())
	#print(io.readuntil(b'letter of guess '))
	x = str(io.readline().replace(b'letter of guess ',b'').strip())
	#x = int(io.readline().strip())
	print(x)
	#print(j)
	#print()
	if x == int(enc_flag[j]):
		print(i)
		flag += i
		continue
