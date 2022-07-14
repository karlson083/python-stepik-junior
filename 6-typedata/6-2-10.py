import os
clear = lambda: os.system('cls')
clear()

s = input()
if 'a' in s:
    print('Введенная строка содержит символ а')
else:
    print('Введенная строка не содержит символ а')

    s = input()
if '.' not in s:
    print('Введенная строка не содержит символа точки')