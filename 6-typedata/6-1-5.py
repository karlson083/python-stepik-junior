import os
clear = lambda: os.system('cls')
clear()

x = float(input())

if x == 0:
    print("Обратного числа не существует")
else:
    print( x ** -1)