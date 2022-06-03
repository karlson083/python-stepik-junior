import os
clear = lambda: os.system('cls')
clear()

a = max(3, 8, -3, 12, 9)
b = min(3, 8, -3, 12, 9)
c = max(3.14, 2.17, 9.8)
print(a)
print(b)
print(c)

print(abs(10))
print(abs(-7))
print(abs(0))
print(abs(-17.67))

num = max(1, 3, -5, 7) + min(-3, 6, -8, -1) + abs(-17)
print(num)