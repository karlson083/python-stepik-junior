
import os
clear = lambda: os.system('cls')
clear()

# объявление функции
def is_magic(date):
    date_list = date.split('.')

    return int(date_list[0]) * int(date_list[1]) == int(date_list[2]) % 100


# считываем данные
date = input()

# вызываем функцию
print(is_magic(date))


'''
def is_magic(date):
    return int(date[:2]) * int(date[3:5]) == int(date[-2:])

date = input()

print(is_magic(date))

'''