import os
clear = lambda: os.system('cls')
clear()

a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input())

if b1 == a2:
    print(b1)
elif a1 <= a2 and b1 > a2 and b1 <= b2:
    print(a2,b1)
elif a1 <= a2 and b1 > a2 and b1 > b2:
    print(a2,b2)
elif a1 <= a2 and b1 > a2 and b1 > b2:
    print(a2,b2)
elif a1 >= a2 and b1 > a2 and b1 > b2:
    print(a1,b1)
else:
    print("пустое множество")