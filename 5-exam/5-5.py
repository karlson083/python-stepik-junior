import os
clear = lambda: os.system('cls')
clear()

x = int(input())

if x % 2 == 0:
    if 2 <= x <= 5:
        print("NO")
    if 6 <= x <= 20:
        print("YES")
    if 20 < x:
        print("NO")
else:
    print("YES")
