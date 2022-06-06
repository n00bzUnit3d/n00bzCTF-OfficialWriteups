#!/usr/bin/env python3
flag = open('flag.txt').read()
f = open('results.txt','w')
for i in range(len(flag)):
	x = input('Enter the flag: \n')
	f.write(str(5**ord(flag[i]) - int(x)) + '\n')
	if 5**ord(flag[i]) - int(x) == 0:
		print(f'Correct letter {flag[i]}')
