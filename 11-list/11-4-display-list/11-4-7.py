import os
clear = lambda: os.system('cls')
clear()

count = 0
#n = int(input())
n = 5
#ls = []
ls = ['Язык Python прекрасен','C# - отличный язык программирования','Stepik - отличная платформа','BEEGEEK FOREVER!','язык Python появился 20 февраля 1991']
'''for i in range(n):
    ls.append(input())'''
#k = int(input())
k = 2
#gs = []
gs = ['язык','python']
out = []
'''for i in range(k):
    gs.append(input())'''
for i in ls:
    for j in gs:
        if j.upper() in i.upper():
            count += 1
        if i not in out and count == k:
                out.append(i)
    count = 0
print(*out, sep='\n')
