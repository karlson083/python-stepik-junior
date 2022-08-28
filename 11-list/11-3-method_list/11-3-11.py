import os
clear = lambda: os.system('cls')
clear()

str = []
n = int(input())
tmpn = int(input())
for _ in range(n-1):
    tmpn2 = int(input())
    str.append(tmpn + tmpn2)
    tmpn = tmpn2
print(str)