import os
clear = lambda: os.system('cls')
clear()


s = str(input())
for i in range(0,len(s),2):
    print(s[i])