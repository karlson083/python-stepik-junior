import os
clear = lambda: os.system('cls')
clear()


s = input()

if s == s.title():
    print("YES")
else:
    print("NO")
