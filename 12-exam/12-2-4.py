import os
from posixpath import split
clear = lambda: os.system('cls')
clear()
'''
s = input().split()
print(s)
for i in range(len(s)):
    s[i] = len(s[i])
print(s)
print(max(s))
'''
print(max([i for i in [len(j) for j in input().split()]]))





print(max([len(a) for a in input().split()]))