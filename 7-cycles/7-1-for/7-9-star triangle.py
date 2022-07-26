import os
clear = lambda: os.system('cls')
clear()

n = int(input())

for i in range(n):
    print("*" * (n-i))