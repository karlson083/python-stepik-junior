from math import pi
import os
from posixpath import split
clear = lambda: os.system('cls')
clear()


from math import pi
# объявление функции
def get_circle(radius):
    return 2 * pi * radius, pi * radius ** 2
    

# считываем данные
r = float(input())

# вызываем функцию
length, square = get_circle(r)
print(length, square)