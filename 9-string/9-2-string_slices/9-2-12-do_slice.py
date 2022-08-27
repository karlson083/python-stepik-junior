import os
clear = lambda: os.system('cls')
clear()

#s = input()
s = "abcdefghijklmnopqrstuvwxyz"

print(str(len(s)))
print(s * 3)
print(s[0])
print(s[:3])
print(s[-3:])
print(s[::-1])
print(s[1:-1])