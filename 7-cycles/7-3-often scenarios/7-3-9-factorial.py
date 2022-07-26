import os
clear = lambda: os.system('cls')
clear()

n = int(input())
nf = 1
for i in range(1, n + 1):
    nf *= i
print(nf)