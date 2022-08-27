from audioop import mul
import os
clear = lambda: os.system('cls')
clear()

text = 'Python'
#text = input()
for i in range(len(text)):
    if i % 3 != 0:
        print(text[i], end = '')
