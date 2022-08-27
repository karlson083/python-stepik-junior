import os
clear = lambda: os.system('cls')
clear()

s = 'abcdefghij'

print(s[2:5])
print(s[0:6])
print(s[2:7])

print(s[2:])
print(s[:7])

print(s[-9:-4])
print(s[-3:])
print(s[:-3])

print(s[::-1])

s = s[:4] + 'X' + s[5:]
print(s)

s = 'abcdefg'
print(s[2:5])

s = 'abcdefg'
print(s[3:])

s = 'abcdefg'
print(s[:3])

s = 'abcdefg'
print(s[:])

s = 'abcdefg'
print(s[::-3])