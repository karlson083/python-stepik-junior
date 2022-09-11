import os
clear = lambda: os.system('cls')
clear()


n = int(input())
ls = []
for i in range(n):
    ls.append(int(input()))
    print(ls[i])
print()
for i in range(len(ls)):
    print(ls[i] ** 2 + 2 * ls[i] + 1)
