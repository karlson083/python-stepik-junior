import os
from posixpath import split
clear = lambda: os.system('cls')
clear()

'''
s = '1 2 3 4 5 6 7 8 9'
#s = input()
l = s.split()
for i in l:
    if int(i) % 2 == 0 and int(i) ** 2 % 10 != 4:
        print(int(i) ** 2, end = ' ')
  '''  



print(*[int(i) ** 2 for i in input().split() if int(i) % 2 == 0 and int(i) ** 2 % 10 != 4])



'''
print(*[i for i in input() if i in ['1','2','3','4','5','6','7','8','9','0']], sep = '')



print(*(i for i in input() if i.isdigit()), sep="")

'''