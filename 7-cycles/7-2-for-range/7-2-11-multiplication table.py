import os
clear = lambda: os.system('cls')
clear()


n = int(input())
for i in range(1, 11):
    print(n, "x", i, "=", n * i)