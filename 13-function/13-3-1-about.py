import os
from posixpath import split
clear = lambda: os.system('cls')
clear()

def print_paris(): 
    s = 'I love Paris'
    print(s) 

def print_london():
    s = 'I love London'
    print(s) 

s = 'I love Moscow'
print_paris()
print_london()
print(s)


def swap(a, b):
    a, b = b, a

a = 4
b = 3
swap(a, b)
print(a - b)


x = 5

def add():
    x = 3
    x = x + 5
    print(x)

add()
print(x)


x = 5

def add():
    global x
    x = 3
    x = x + 5
    print(x)

add()
print(x)