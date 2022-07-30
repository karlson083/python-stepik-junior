import os
clear = lambda: os.system('cls')
clear()

y = ''
#x = str(input())
x = 5
while x > 0:
    y = str(x % 2) + y
    x //= 2
print(y)
