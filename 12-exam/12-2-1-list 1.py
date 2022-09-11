import os
from posixpath import split
clear = lambda: os.system('cls')
clear()


print([i for i in range(1,int(input())+1) if int(i) % 2 == 0])

print(list(range(2, int(input()) + 1, 2)))