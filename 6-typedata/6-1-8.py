import os
clear = lambda: os.system('cls')
clear()

x = float(input())

y = int(x *10 % 10)

print(y)