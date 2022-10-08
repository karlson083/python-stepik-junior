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
#elif a1 >= a2 and b1 > a2 and b1 > b2:
#   print(a1,b1)
elif a1 >= a2 and b1 > a2 and b1 <= b2:
    print(a1,b1)
elif a1 >= a2 and b2 > a1 and b1 >= b2:
    print(a1,b2)
elif a1 == b2:
    print(a1)

else:
    print("пустое множество")


    '''
    a1, b1, a2, b2 = int(input()), int(input()), int(input()), int(input()) 
if min(b1, b2) < max(a1, a2): 
    print('пустое множество')
elif min(b1, b2) == max(a1, a2):
    print(min(b1, b2))
else:
    print(max(a1, a2), min(b1, b2))
    
    '''