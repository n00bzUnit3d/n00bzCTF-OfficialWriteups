import os
print("Welcome to Jail You can't escape!")
# Flag is in /secret/verysecret/flag.txt
print('-'*10)
print(open(__file__).read())
print('-'*10)
while True:
    x = input(">>> ")
    whitelist = ["0","1","2","3","4","5","6","7","8","9","/","*","?","$",".","'","!","@","#"]
    for i in range(11):
        whitelist += whitelist[i].upper()
    if any([i for i in x if i not in whitelist]):
        print("I see you are trying to hack, Exiting!")
        exit(0)
    else:
        os.system(x)


