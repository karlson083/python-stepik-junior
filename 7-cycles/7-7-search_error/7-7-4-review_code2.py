import os
clear = lambda: os.system('cls')
clear()

mx = -10**6 - 1
s = 0
for i in range(1,11):#
    x = int(input())
    if x < 0:
        s += x#
    if x < 0 and x > mx:
        mx = x
if s < 0: 
    print(s)
    print(mx)
else:
    print('NO')