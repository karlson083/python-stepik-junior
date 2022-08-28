import os
clear = lambda: os.system('cls')
clear()

str = []
n = int(input())
for _ in range(n):
    tmps = input()
    str.append(tmps)
print(str)