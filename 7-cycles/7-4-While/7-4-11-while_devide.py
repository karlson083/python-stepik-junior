import os
clear = lambda: os.system('cls')
clear()


x = int(input())
while x % 7 == 0:
    print(x)
    x = int(input())
    