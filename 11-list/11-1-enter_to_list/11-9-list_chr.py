import os
clear = lambda: os.system('cls')
clear()


n = 10
#n = int(input())
ls = ''
for i in range(97,n+97):
    ls += chr(i)
lst = list(ls)
print(lst)
