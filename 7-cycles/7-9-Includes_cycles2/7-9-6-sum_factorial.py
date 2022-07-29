from msvcrt import kbhit
import os
clear = lambda: os.system('cls')
clear()

n = int(input())
summ = 0
fact = 1
for i in range(1,n+1):
    for j in range(1,i+1):
        fact *= j
    summ += fact
    fact = 1
print(summ)



n = int(input())
a = 1
b = 0
for i in range(1, n + 1):
    a *= i
    b += a
print(b)