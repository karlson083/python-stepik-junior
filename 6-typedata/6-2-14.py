import os
clear = lambda: os.system('cls')
clear()

s = input()

if '@' in s and '.' in s:
    print('YES')
else:
    print('NO')