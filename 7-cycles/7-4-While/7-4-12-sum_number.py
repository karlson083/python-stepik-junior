
import os
clear = lambda: os.system('cls')
clear()

count = 0
x = int(input())
while x >= 0:
    count += x
    x = int(input())
print(count)


