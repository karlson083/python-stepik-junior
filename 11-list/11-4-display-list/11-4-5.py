import os
clear = lambda: os.system('cls')
clear()


n = int(input())
numbers = []
for i in range(n):
    s = input()
    if s not in numbers:
        numbers.append(s)
print(*numbers, sep='\n')