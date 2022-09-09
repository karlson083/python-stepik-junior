import os
clear = lambda: os.system('cls')
clear()

s = input()
words = s.split()
for i in words:
    print(i[0], end='.')
