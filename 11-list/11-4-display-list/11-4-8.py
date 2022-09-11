import os
clear = lambda: os.system('cls')
clear()

#n = int(input())
n = 5
#ls = []
ls = [3,-4,1,0,-1,0,-2]
'''for i in range(n):
    ls.append(int(input()))'''
for i in ls:
    if i < 0:
        print(i)
for i in ls:
    if i == 0:
        print(i)
for i in ls:
    if i > 0:
        print(i)


n = int(input())
x = [int(input()) for _ in range(n)]
[print(i) for i in x if i < 0]
[print(i) for i in x if i == 0]
[print(i) for i in x if i > 0]