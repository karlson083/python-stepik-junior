from msvcrt import kbhit
import os
clear = lambda: os.system('cls')
clear()

a = int(input())
b = int(input())
if a == 1:
    a = 2
for i in range(a,b+1):
    count = 0
    for j in range(1,i+1):
        if i % j == 0:
            count += 1
    if count == 2:
        print(i)
    