import os
clear = lambda: os.system('cls')
clear()

str = []
n = 26
for i in range(n):
    str.append(chr(i+97) * (i+1))
print(str)


print([chr(97 + i) * (i + 1) for i in range(26)])