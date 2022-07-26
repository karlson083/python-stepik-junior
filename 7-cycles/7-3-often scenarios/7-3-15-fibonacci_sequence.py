import os
from tkinter import Y
clear = lambda: os.system('cls')
clear()


n = int(input())
x = 0
y = 1
print("1", end=' ')
for _ in range(n-1):
    z = y + x
    x = y
    y = z
    print(z, end=' ')

#################################


n = int(input())
a, b = 1, 1

for i in range(n):
    print(a, end=' ')
    a, b = b, a + b
