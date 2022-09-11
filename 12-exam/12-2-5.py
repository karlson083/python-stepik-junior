import os
from posixpath import split
clear = lambda: os.system('cls')
clear()

'''
s = input().split()
for i in s:
    print(i[1:], i[0],'ки', sep = '', end = ' ')
'''
print(*[i[1:]+i[0]+'ки' for i in input().split()])