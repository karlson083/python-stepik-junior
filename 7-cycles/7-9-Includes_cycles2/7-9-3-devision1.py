from msvcrt import kbhit
import os
clear = lambda: os.system('cls')
clear()

sumdevision = 0
sumdevision_tmp = 0
a = int(input())
b = int(input())
xmax = a
for i in range(a,b+1):
    for j in range(i,0,-1):
        if i % j == 0:
            sumdevision_tmp += j
    if sumdevision_tmp > sumdevision:
        sumdevision = sumdevision_tmp
        xmax = i
    elif sumdevision_tmp == sumdevision:
        sumdevision = sumdevision_tmp
        if i > xmax:
            xmax = i
    sumdevision_tmp = 0
print(xmax, sumdevision)