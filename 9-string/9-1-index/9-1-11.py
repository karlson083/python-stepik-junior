import os
clear = lambda: os.system('cls')
clear()

summ = 'Цифр нет'
s = str(input())
for c in s:
    if c in ['0','1','2','3','4','5','6','7','8','9']:
        summ = 'Цифра'
        break
print(summ)