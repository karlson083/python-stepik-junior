import os
clear = lambda: os.system('cls')
clear()

count = 0
for _ in range(10):
    x = int(input())
    if x % 2 != 0:
        count += 1
if count == 0:
    print("YES")
else:
    print("NO")
