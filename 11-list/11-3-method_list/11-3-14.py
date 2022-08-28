import os
clear = lambda: os.system('cls')
clear()

str = []
str2 = []
n = int(input())
for _ in range(n):
    str.append(input())

for i  in range(n):
    str2.extend(str[i])
print(str2)




n = int(input())
sp = []
for _ in range(n):
    sp.extend(input())
print(sp)