from audioop import mul
import os
clear = lambda: os.system('cls')
clear()

#a, b = 65, 70
a, b = int(input()), int(input())
for i in range(a,b+1):
    print(chr(i), end = ' ')