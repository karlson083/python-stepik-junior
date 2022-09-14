import os
from posixpath import split
clear = lambda: os.system('cls')
clear()

# объявление функции
def get_days(month):
    days = 0
    if month in [1,3,5,7,8,10,12]:
        days = 31
    elif month in [4,6,9,11]:
        days = 30
    else:
        days = 28
    return days
    

# считываем данные
num = int(input())

# вызываем функцию
print(get_days(num))




def get_days(month):
    m = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    return m[month - 1]
# считываем данные
num = int(input())

# вызываем функцию
print(get_days(num))



def get_days(month):
    return (28 if month == 2 else 30 if month in [4, 6, 9, 11] else 31)
num = int(input()) # считываем данные
print(get_days(num)) # вызываем функцию