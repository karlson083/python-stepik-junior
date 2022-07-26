import os
clear = lambda: os.system('cls')
clear()

n = int(input())
sum = 0
for _ in range(n):
    x = int(input())
    sum += x
print(sum)