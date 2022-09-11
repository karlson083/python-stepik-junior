import os
from posixpath import split
clear = lambda: os.system('cls')
clear()

def print_number(a, b, c):
    d = (a + c) // b
    print(d)

print_number(2, 3, 11)

def change_us(a, b):
    a = 0
    b = 0
    print(a, b)

x = 1
y = 7
print(x, y)
change_us(x, y)
print(x, y)

def print_text(text, num):
    while num > 0:
        print(text, end='')
        num -= 1

print_text('Python', 4)