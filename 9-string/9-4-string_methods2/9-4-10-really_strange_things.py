import os
clear = lambda: os.system('cls')
clear()

#n = int(input())
n = 3
count = 0
for _ in range(n):
    s = input()
    if s.count('11') > 2:
        count += 1
print(count)
