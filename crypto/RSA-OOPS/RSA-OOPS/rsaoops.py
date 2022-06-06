#!/usr/local/bin/python
#
# Polymero
#

# Imports
from Crypto.Util.number import getPrime, inverse
import os, random

# Local imports
with open('flag.txt', 'rb') as f:
    FLAG = f.read()
    f.close()


# Challenge class:
class RSAOOPS1024:

    def __init__(self):
        """ Generate RSA keys and entropy pool. """
        # Chunk sizes
        self.KL = round(1024 / 5 * 4)
        self.KR = round(1024 / 5 * 1)

        # RSA key for L chunk
        self.EL = 17
        while True:
            PL, QL = [getPrime(self.KL // 2) for _ in '01']
            self.DL = inverse(self.EL, (PL - 1)*(QL - 1))
            if self.DL != 1:
                self.NL = PL * QL
                break

        # RSA key for R chunk
        self.ER = 0x10001
        while True:
            PR, QR = [getPrime(self.KR // 2) for _ in '01']
            self.DR = inverse(self.ER, (PR - 1)*(QR - 1))
            if self.DR != 1:
                self.NR = PR * QR
                break

        # Entropy pool
        rng = random.Random(SERVER_SEED)
        self.pool = [rng.getrandbits(self.NR.bit_length() - 1) for _ in range(128)]
        random.shuffle(self.pool)

    def __repr__(self):
        """ Representation string. """
        pubkey = ((self.NL << self.KR) + self.NR).to_bytes(128, 'big').hex()
        return "RSA-OOPS-1024 ({} left) with public key N = {}".format(len(self.pool), pubkey)

    def encrypt(self, m):
        """ RSA-OOPS-1024 encryption. """
        m_int = int.from_bytes(m, 'big')
        r_int = self.pool.pop(0)
        X = pow(m_int + r_int, self.EL, self.NL)
        Y = pow(X, self.DR, self.NR) ^ r_int
        return (X << self.KR) + Y

    def decrypt(self, XY):
        """ RSA-OOPS-1024 decryption. """
        X = XY >> self.KR
        Y = XY & (2**self.KR - 1)
        r = Y ^ pow(X, self.DR, self.NR)
        m = pow(X, self.DL, self.NL) - r
        return m.to_bytes(128, 'big').lstrip(b"\x00")


# Server loop
HDR = r"""|
|
|    (    (                 )     )  (    (     
|    )\ ) )\ )   (       ( /(  ( /(  )\ ) )\ )  
|   (()/((()/(   )\      )\()) )\())(()/((()/(  
|    /(_))/(_)|(((_)(   ((_)\ ((_)\  /(_))/(_)) 
|   (_)) (_))  )\ _ )\   ((_)  ((_) (_)) (_))   
|   | _ \/ __| (_)_\(_)  / _ \ / _ \| _ \/ __|  
|   |   /\__ \  / _ \   | (_) | (_) |  _/\__ \  
|   |_|_\|___/ /_/ \_\   \___/ \___/|_|  |___/  
|"""

print(HDR)

SERVER_SEED = int.from_bytes(os.urandom(32), 'big')

oop = RSAOOPS1024()

while True:

    try:

        if not oop.pool:

            print('|\n|  You have exhausted the entroopsy pool.')
            print('|   [C]onstruct new instance\n|   [Q]uit')
            choice = input('|\n|  >> ').lower()

            if choice == 'c':
                oop = RSAOOPS1024()

            elif choice == 'q':
                raise KeyboardInterrupt

            else:
                continue

        print('|\n|  {}'.format(oop))
        print('|\n|   [E]ncrypt flag\n|   [Q]uit')
        choice = input('|\n|  >> ').lower()

        if choice == 'e':
            flag = oop.encrypt(FLAG).to_bytes(128, 'big').hex()
            print("|\n|  {}".format(flag))

        elif choice == 'q':
            raise KeyboardInterrupt

        else:
            continue

    except KeyboardInterrupt:
        print("|\n|\n|  Bye ~ !\n|")
        break

    except:
        print("|\n|  Something went wrong...")
        continue