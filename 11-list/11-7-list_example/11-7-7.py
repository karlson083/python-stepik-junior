import os
clear = lambda: os.system('cls')
clear()

n = int(input())
square = [(i+1) ** 2 for i in range(n)]

print(*square, sep = '\n')