import os
clear = lambda: os.system('cls')
clear()

m = int(input())
p = int(input())
n = int(input())

for i in range(n):
    print(i+1, m)
    m = m * (1+p/100)
    