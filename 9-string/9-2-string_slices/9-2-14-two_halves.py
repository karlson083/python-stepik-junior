import os
clear = lambda: os.system('cls')
clear()

#s = input()
s = "a"
l = len(s)
l2 = int(len(s) / 2)
if l % 2 == 0:
    print(s[l2:l] + s[0:l2])
else:
    print(s[l2+1:l] + s[0:l2+1])
