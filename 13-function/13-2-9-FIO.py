import os
from posixpath import split
clear = lambda: os.system('cls')
clear()


# объявление функции
def print_fio(name, surname, patronymic):
    print(surname[0].upper(), name[0].upper(), patronymic[0].upper(), sep = '')





# считываем данные
name, surname, patronymic = input(), input(), input()

# вызываем функцию
print_fio(name, surname, patronymic)




'''FIO'''# объявление функции
def print_fio(name, surname, patronymic):
    print(f"{surname[0]}{name[0]}{patronymic[0]}".upper())


name, surname, patronymic = input(), input(), input(),
print_fio(name, surname, patronymic)




# объявление функции
def print_fio(name, surname, patronymic):
    print((surname[0]+name[0]+patronymic[0]).upper())
    pass

# считываем данные
name, surname, patronymic = input(), input(), input(),

# вызываем функцию
print_fio(name, surname, patronymic)