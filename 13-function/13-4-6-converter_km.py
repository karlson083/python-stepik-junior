import os
from posixpath import split
clear = lambda: os.system('cls')
clear()

# объявление функции
def convert_to_miles(km):
    ml = km * 0.6214
    return ml
# считываем данные
num = int(input())

# вызываем функцию
print(convert_to_miles(num))