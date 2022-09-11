import os
clear = lambda: os.system('cls')
clear()


n = int(input())
ls = []
for i in range(n):
    ls.append(input())
google_search = input()
for i in range(len(ls)):
    tmp = ls[i]
    if google_search.upper() in tmp.upper():
        print(ls[i])
