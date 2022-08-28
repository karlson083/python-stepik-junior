import os
clear = lambda: os.system('cls')
clear()

str = []
n = int(input())
for _ in range(n):
    tmps = int(input())
    str.append(tmps ** 3)
print(str)