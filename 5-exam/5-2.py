import os
clear = lambda: os.system('cls')
clear()

x1 , y1 , x2 , y2 = int(input()), int(input()), int(input()), int(input())

if x1 % 2 != 0:
    if y1 % 2 != 0:
        k1 = 1
    else:
        k1 = 0
else:
    if y1 % 2 != 0:
        k1 = 0
    else:
        k1 = 1

if x2 % 2 != 0:
    if y2 % 2 != 0:
        k2 = 1
    else:
        k2 = 0
else:
    if y2 % 2 != 0:
        k2 = 0
    else:
        k2 = 1
if k1 == k2:
    print("YES")
else:
    print("NO")
