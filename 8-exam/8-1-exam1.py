import os
clear = lambda: os.system('cls')
clear()

n = int(input())
res = 1
i = 2
while i <= n:
    res *= i
    i += 1
print(res)