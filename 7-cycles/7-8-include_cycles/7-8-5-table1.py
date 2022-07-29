import os
clear = lambda: os.system('cls')
clear()

n = int(input())
for _ in range(n):
    for _ in range(3):
        print(n, end=' ')
    print('', end ='\n')