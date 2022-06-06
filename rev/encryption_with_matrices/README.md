# encryption_with_matrices | NoobMaster
- Description: I made this encryption scheme using matrices but he didn't make the decryption scheme, Please help me decrypt this message!

chall:/attachments/encryption_with_matrices/chall.py

# Write up

solve - 
```py
enc=[21629584900, 4118558976, 4118558976, 17167812676, 26606176996, 27044131401, 5407396225, 19334346304, 4291953169, 23640600025, 16132810225, 23640600025, 17519963769, 19334346304, 4649466969, 21238107289, 4649466969, 16132810225, 24053528464, 4118558976, 4118558976, 20465877481, 16132810225, 21238107289, 4649466969, 16132810225, 21238107289, 4118558976, 23231246724, 4649466969, 16132810225, 24053528464, 19334346304, 4833586576, 21629584900, 16132810225, 18597867876, 4291953169, 24890110756, 4649466969, 16132810225, 19334346304, 4118558976, 24470032041, 23231246724, 23640600025, 16132810225, 24053528464, 4118558976, 16132810225, 21238107289, 4833586576, 20465877481, 4649466969, 16132810225, 4833586576, 21629584900, 17875690000, 16132810225, 5021281321, 16132810225, 21238107289, 4291953169, 21629584900, 24470032041, 24053528464, 4649466969, 23640600025, 16132810225, 24053528464, 4118558976, 16132810225, 23640600025, 4118558976, 20850204816, 24890110756, 4649466969, 16132810225, 25740993600, 8265719056, 8265719056, 27930765625]
import sympy
flag = ''
for i in enc:
    x = i//1337
    y = x//1337
    
    char = sympy.sqrt(y)
    flag += chr(char)
print(flag)
```
Output - n00bz{7h1s_sch3m3_t00k_m3_m0r3_th4n_f1v3_h0urs_t0_m4k3_4nd_5_m1nut3s_t0_s0lv3_xDD}
So the encryption scheme is as follows - 
Step 1) Multiply both the elements in both matrices for eg - 
[110,110] = [12100] or [[110,110][48,48]] = [[12100,2304]]
Step 2) Multiply element 1 of matrix 1 by element 1 of matrix 2 for eg - 
[1337,1337] * [110,110] after encrypting once becomes [12100,1787569]
Which then multiplied becomes 12100 * 1787569 = 21629584900 which is the first element in the final cipher text.
So the decryption scheme is as follows - 
Step 1) Given 21629584900 as first element of ct and 1337 as element of the matrix 2 - 
```py
result = 21629584900 / 1337
print(result / 1337)
```
Which will print 12100 now after looking at the code, both the elements of the matrix are same(sorry if it's confusing, I mean [110,110] and not for eg [110,48]).
Step 2) So we know that it has to be a square root of some number so using sympy we calulate sqrt(short for square root) which gives us 110, and then chr(110) gives `n` which is part of the flag format `n00bz{`
A for loop to do this and get the flag is listed above

# Flag - n00bz{7h1s_sch3m3_t00k_m3_m0r3_th4n_f1v3_h0urs_t0_m4k3_4nd_5_m1nut3s_t0_s0lv3_xDD}
