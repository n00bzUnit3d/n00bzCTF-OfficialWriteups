#!/usr/bin/env python3
#
# Polymero
#

# Imports
from pwn import *
from sage.all import prime_factors, inverse_mod, crt, gcd

# Connection
host = "0.0.0.0"
port = 5000

s = remote(host, port)

#context.log_level = "debug"

KL = round(1024 / 5 * 4)
KR = round(1024 / 5 * 1)

NLs = []
NRs = []
X17dics = []

n = 17
print('Starting...', end='\r', flush=True)

while True:

	s.recvuntil(b"N = ")
	N = int(s.recvuntil(b"\n", drop=True).decode(), 16)

	nl = N >> KR
	nr = N & (2**KR - 1)

	encs = []

	for _ in range(128):

		s.recv()
		s.sendline(b"e")

		s.recvuntil(b"|  ")
		encs += [int(s.recvuntil(b"\n", drop=True).decode(), 16)]

	Xs = [i >> KR for i in encs]
	Ys = [i & (2**KR - 1) for i in encs]

	pq = prime_factors(nr)
	dr = inverse_mod(0x10001, (pq[0] - 1) * (pq[1] - 1))

	rs = [Ys[i] ^ int(pow(Xs[i], dr, nr)) for i in range(128)]

	X17dic = { rs[i] : Xs[i] for i in range(128) }

	NLs += [nl]
	NRs += [nr]
	X17dics += [X17dic]

	l203, l204 = [len([i for i in NRs if i.bit_length() == j]) for j in [203, 204]]

	print("203: {:2d}/{n}   204: {:2d}/{n}".format(l203, l204, n=n), end='\r', flush=True)

	if l203 >= n:
		bitlen = 203
		break

	if l204 >= n:
		bitlen = 204
		break

	s.recv()
	s.sendline(b"c")

NLs_bitlen = [NLs[i]     for i in range(len(NLs)) if NRs[i].bit_length() == bitlen]
X17_bitlen = [X17dics[i] for i in range(len(NLs)) if NRs[i].bit_length() == bitlen]

ret = []

for i in range(5):

	r = list(X17_bitlen[0].keys())[i]

	X17s = [int(j[r]) for j in X17_bitlen]

	X17_full = crt(X17s, NLs_bitlen)

	ret += [X17_full - int(pow(r, 17))]

m_rec = ret[0]
for i in range(1, len(ret)):
	m_rec = gcd(m_rec, ret[i])

print(int(m_rec).to_bytes(128, 'big').lstrip(b"\x00"))