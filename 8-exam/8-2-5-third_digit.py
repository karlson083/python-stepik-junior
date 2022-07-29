import os
clear = lambda: os.system('cls')
clear()

n = int(input())
while n > 999:
    n //= 10
print(n % 10)