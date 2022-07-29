import os
clear = lambda: os.system('cls')
clear()

n = int(input())
for i in range(1,n+1):
    for j in range(1,10):
        print(i, '+', j, '=', i+j)
    print()