import os
clear = lambda: os.system('cls')
clear()

n = int(input())
sums = 0
for i in range(1, n +1):
    if i ** 2 % 10 in [2, 5, 8]:
        sums += i
print(sums)