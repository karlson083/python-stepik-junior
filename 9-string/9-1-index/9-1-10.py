import os
clear = lambda: os.system('cls')
clear()

summ = 0
s = str(input())
for c in s:
    summ += int(c)
print(summ)