import os
clear = lambda: os.system('cls')
clear()

x1 , y1 , x2 , y2 = int(input()), int(input()), int(input()), int(input())

if (x1==x2 and y1!=y2) or (x1!=x2 and y1==y2) or abs(x1-x2) == abs(x1-x2):
    print("YES")
else:
    print("NO")


 