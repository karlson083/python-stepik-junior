import os
clear = lambda: os.system('cls')
clear()

s = input()
words = s.split('\\')
print(*words, sep='\n')
