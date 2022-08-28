import os
clear = lambda: os.system('cls')
clear()

str = []
n = int(input())
for _ in range(n):
    str.append(int(input()))
del str[1:n:2]
print(str)