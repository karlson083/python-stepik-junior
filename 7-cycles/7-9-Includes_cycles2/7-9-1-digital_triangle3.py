import os
clear = lambda: os.system('cls')
clear()

count = 0
n = int(input())
for i in range(1,n+1):
    for _ in range(1,i+1):
        count += 1
        print(count, end = ' ')
    print()