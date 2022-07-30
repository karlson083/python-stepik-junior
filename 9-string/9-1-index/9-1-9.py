import os
clear = lambda: os.system('cls')
clear()


stm = ''
for _ in range(3):
    s = str(input())
    stm += s[0]
print(stm[1] + stm[0] + stm[2])