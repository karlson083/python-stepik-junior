import os
clear = lambda: os.system('cls')
clear()

x = int(input())

if x == 0:
    print("зеленый")
elif 1 <= x <= 10:
    if x % 2 != 0:
        print("красный")
    else:
        print("черный")
elif 11 <= x <= 18:
    if x % 2 == 0:
        print("красный")
    else:
        print("черный")
elif 19 <= x <= 28:
    if x % 2 != 0:
        print("красный")
    else:
        print("черный")
elif 29 <= x <= 36:
    if x % 2 == 0:
        print("красный")
    else:
        print("черный")
else:
    print("ошибка ввода")