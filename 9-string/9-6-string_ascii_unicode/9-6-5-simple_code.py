from audioop import mul
import os
clear = lambda: os.system('cls')
clear()

text = "Hello world!"
#text = input()
for i in text:
    print(ord(i), end = ' ')