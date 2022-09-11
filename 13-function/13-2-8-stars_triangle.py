import os
from posixpath import split
clear = lambda: os.system('cls')
clear()


def draw_triangle(fill, base):
    for i in range(1,int((base+1)/2+1)):
        print(fill * i)
    for i in range(int((base-1)/2),0,-1):
        print(fill * i)
fill = input()
base = int(input())
draw_triangle(fill, base)



# объявление функции
def draw_triangle(fill, base):
    for i in range(1, base + 1):
        print(fill * min(i, base - i + 1))

# считываем данные
fill = input()
base = int(input())

# вызываем функцию
draw_triangle(fill, base)