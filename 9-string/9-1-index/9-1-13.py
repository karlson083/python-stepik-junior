import os
clear = lambda: os.system('cls')
clear()

summ_same = 0
#s = str(input())
s = 'aabbcc'
for i in range(0,len(s)-1):
    if s[i] == s[i+1]:
        summ_same += 1
print(summ_same)
