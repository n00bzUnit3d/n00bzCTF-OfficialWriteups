#!/usr/local/bin/python
#
# Polymero
#

# Imports
from Crypto.Util.number import getPrime, inverse
from secrets import randbelow

# Local imports
with open("flag.txt",'rb') as f:
    FLAG = f.read()
    f.close()


# Header
HDR = r"""|
|              ______
|             /\  == \
|             \ \  _-/
|              \ \_\
|               \/_/
|   __  __     ______     _____     __     ______
|  /\ \_\ \   /\  __ \   /\  __-.  /\ \   /\  ___\
|  \ \  __ \  \ \  __ \  \ \ \/\ \ \ \ \  \ \___  \
|   \ \_\ \_\  \ \_\ \_\  \ \____-  \ \_\  \/\_____\
|    \/_/\/_/   \/_/\/_/   \/____/   \/_/   \/_____/
|                __
|               /\ \
|               \ \ \
|                \ \_\
|                 \/_/
|              _____
|             /\  __-.
|             \ \ \/\ \
|              \ \____-
|               \/____/
|              ______
|             /\  ___\
|             \ \  __\
|              \ \_____\
|               \/_____/
|"""


# Challenge Class
class HadisPaide:

    def __init__(self):
        """ Create Paillier key and game parameters. """
        P, Q = [getPrime(512) for _ in '01']
        self.N = P * Q
        self.L = (P - 1) * (Q - 1)
        self.G = randbelow(self.N * self.N)
        self.U = inverse((pow(self.G, self.L, self.N * self.N) - 1) // self.N, self.N)
        
        self.HADIS = int.from_bytes(FLAG,'big')
        self.PAIDE = None

    def free(self, x):
        """ Return a single free encryption of input integer. """
        assert (x > 0) and (x < self.N)
        g_m = pow(self.G, x, self.N * self.N)
        r_n = pow(randbelow(self.N), self.N, self.N * self.N)
        return (g_m * r_n) % (self.N * self.N)
        
    def play(self, x):
        """ Return whether you are warmer or colder to the flag. ^w^ """
        assert (x > 0) and (x < self.N * self.N)
        d = ((pow(x, self.L, self.N * self.N) - 1) // self.N * self.U) % self.N
        h = sum([1 for i in list(bin(d ^ self.HADIS)[2:]) if i == '1'])
        if not self.PAIDE or self.PAIDE == h:
            out = '...'
        elif h < self.PAIDE:
            out = 'Warmer ~'
        elif h > self.PAIDE:
            out = 'Colder...'
        self.PAIDE = h
        return out

    
# Server Loop
print(HDR)

hapa = HadisPaide()

print("| N:", hapa.N)

try:

    print("|\n|  You get ONE free encryption. What will it be?")

    x = int(input("|\n|  x: "))
    print("|\n| ", hapa.free(x))

    print("|\n|\n|  Alright, time to play!")

except:
    print("|\n|  Something went wrong... Are you playing by the rules?")

while True:
    try:
        
        print("|\n|\n| [P]lay")
        print("| [Q]uit")
        
        choice = input("|\n|  >> ").lower()
        
        if choice == 'p':
            x = int(input("|\n|  x: "))
            print("|\n| ", hapa.play(x))
            
        elif choice == 'q':
            raise KeyboardInterrupt
            
        else:
            print("|\n|  That's not an option. Try again.")
        
    except KeyboardInterrupt:
        print("|\n|\n|  Vale ~ \n|")
        break
        
    except:
        print("|\n|  Something went wrong... Are you playing by the rules?")
