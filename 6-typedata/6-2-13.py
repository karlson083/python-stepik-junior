import os
clear = lambda: os.system('cls')
clear()

s = input()

if 'суббота' in s:
    print('YES')
elif 'воскресенье' in s:
    print('YES')
else:
    print('NO')