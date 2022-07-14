import os
clear = lambda: os.system('cls')
clear()

s = input()

if 'синий' in s:
    print('YES')
else:
    print('NO')