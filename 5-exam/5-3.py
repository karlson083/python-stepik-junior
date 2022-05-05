import os
clear = lambda: os.system('cls')
clear()

y = int(input())
p = input()

if p == "f":
    if 10 <= y <= 15:
        print("YES")
    else:
        print("NO")
else:
    print("NO")