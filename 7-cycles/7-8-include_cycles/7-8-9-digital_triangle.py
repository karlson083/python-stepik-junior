import os
clear = lambda: os.system('cls')
clear()

n = int(input())
for i in range(1,n+1):
    print(str(i)*i)