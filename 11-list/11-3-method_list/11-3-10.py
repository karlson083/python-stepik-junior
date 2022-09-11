import os
clear = lambda: os.system('cls')
clear()

str = []
n = int(input())
for i in range(1, n+1):
    if n % i == 0:
        str.append(i)
print(str)