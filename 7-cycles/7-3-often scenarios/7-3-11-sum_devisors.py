import os
clear = lambda: os.system('cls')
clear()

result = 0
n = int(input())
for i in range(1, n + 1):
    if n % i == 0:
        result += i
print(result)