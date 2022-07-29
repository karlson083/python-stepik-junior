import os
clear = lambda: os.system('cls')
clear()

n = int(input())
for i in range(1,int(((n+1)/2)+1)):
    print('*'*i)
for j in range(int((n-1)/2),0,-1):
    print('*'*j)


n = int(input())
for i in range(n):
    k = (n // 2 + 1) - abs(n // 2 - i)
    for _ in range(k):
        print('*', end='')
    print()