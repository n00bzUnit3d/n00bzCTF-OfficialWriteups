# the ways of php | GamingChair

- Description: I created this simple site for you. I'm not good at making keys, but I'm secure enough, right?
- Hint: The key is the same as the challenge author name (GamingChair)

remote:http://159.65.232.9:42068/

# Write up

First thing is lfi by using glob:// php wrapper. The brute is in solve/brute.py . File numeration shows us 9 files, some of them are just dummy files. The import ones are WzNsbej4VS.php - the login page and qHkldgoTQ4.tar - the backup file of the login page

The vulnerability in the login is bcrypt misuse by pre-hashing password before supplying it to password_hash and password_verify, the details are here in this blog post: https://blog.ircmaxell.com/2015/03/security-issue-combining-bcrypt-with.html The description hints at the key - the author of the challenge - GamingChair . To bruteforce possible passwords: solve/login_solve.php

# Flag - n00bz{D0nt_c0mb1n3_wh4t5_n0t_m34nt_t0_b3_c0mb1n3d}

