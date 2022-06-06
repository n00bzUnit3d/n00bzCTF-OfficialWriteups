#!/usr/bin/env python3

from pwn import p32
from zlib import crc32
required_crc = 0xEC891D43
max_dimension = 4000
for height in range(600,1000):
	for width in range(1300,2000):
		ihdr = b'\x49\x48\x44\x52' + p32(width, endian='big') + p32(height, endian='big') + b'\x08\x02\x00\x00\x00'
		crc = crc32(ihdr)
		print(hex(crc))
		print(width,height)
		if crc == required_crc:
			print('Found width and height!')
			print(width,height)
			exit(0)