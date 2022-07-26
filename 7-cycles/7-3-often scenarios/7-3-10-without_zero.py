import os
clear = lambda: os.system('cls')
clear()

result = 1
for _ in range(10):
    x = int(input())
    if x != 0:
        result *= x
print(result)