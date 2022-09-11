import os
from posixpath import split
clear = lambda: os.system('cls')
clear()

sl = input().split()
s = '+'.join(sl)
for i in range(len(sl)):
    sl[i] = int(sl[i])
print(s,'=',sum(sl), sep = '')





n = [int(i) for i in input().split()]
print(*n, sep='+', end='=')
print(sum(n))