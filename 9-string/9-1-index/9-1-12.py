import os
clear = lambda: os.system('cls')
clear()

summ_plus = 0
summ_multi = 0
#s = str(input())
s = 'bcd+a++++**31415'
for c in s:
    if c == '+':
        summ_plus += 1
    if c == '*':
        summ_multi += 1
print('Символ + встречается', summ_plus, 'раз')
print('Символ * встречается', summ_multi, 'раз')