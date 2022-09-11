import os
from posixpath import split
clear = lambda: os.system('cls')
clear()

'''
s = input()
for i in s:
    if i in ['1','2','3','4','5','6','7','8','9','0']:
        print(i, end = '')
'''
print(*[i for i in input() if i in ['1','2','3','4','5','6','7','8','9','0']], sep = '')



print(*(i for i in input() if i.isdigit()), sep="")