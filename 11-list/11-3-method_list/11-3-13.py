import os
clear = lambda: os.system('cls')
clear()

str = []
n = int(input())
for _ in range(n):
    str.append(input())
k = int(input())

for i  in range(n):
    if len(str[i]) >= k:
        tmps = str[i] 
        print(tmps[k-1] , end = '')
