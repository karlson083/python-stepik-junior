import os
clear = lambda: os.system('cls')
clear()

first = 0
second = 0
n = int(input())
for _ in range(n):
    x = int(input())
    if x > first:
        second = first
        first = x
    elif x > second:
        second = x
print(first)
print(second)
