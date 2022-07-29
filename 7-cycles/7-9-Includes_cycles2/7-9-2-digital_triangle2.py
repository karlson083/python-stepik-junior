from msvcrt import kbhit
import os
clear = lambda: os.system('cls')
clear()


n = int(input())
print(1)
for i in range(1,n):
    for j in range(1,i+2):
        print(j, end = '')
    for k in range(j-1,0,-1):
        print(k, end = '')
    print()