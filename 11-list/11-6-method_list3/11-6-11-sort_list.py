import os
from posixpath import split
clear = lambda: os.system('cls')
clear()

s = '4 5 1 2 3 8'
#s = input()
ss = s.split()
for i in range(len(ss)):
    ss[i] = int(ss[i])
ss.sort()
print(*ss, sep= ' ')
ss.sort(reverse=True)
print(*ss, sep= ' ')
