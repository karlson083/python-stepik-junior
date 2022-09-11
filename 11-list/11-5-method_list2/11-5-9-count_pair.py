import os
clear = lambda: os.system('cls')
clear()

s = '3 3 3 3 3'
#s = input()
count = 0
ss = s.split()
for i in range (len(ss)-1):
    for j in range (i+1,len(ss)):
        print(i,j,ss[i] , ss[j])
        if ss[i] == ss[j]:
            count += 1
print(count)
