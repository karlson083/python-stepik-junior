import os
clear = lambda: os.system('cls')
clear()

s = 'qwerty and password'
d = '**'
#s = input()
#d = input()
ss = list(s)
print(*ss, sep=d)
