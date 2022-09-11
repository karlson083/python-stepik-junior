import os
from posixpath import split
clear = lambda: os.system('cls')
clear()

numbers = [1, 2, 3, 4, 5]
numbers[2] = 99
print(numbers)

numbers = list(range(3))
print(numbers)

numbers = list(range(1, 10, 2))
for i in numbers:
    print(i, end='*')

numbers = [1, 2, 3, 4, 5]
print(numbers[-2])

numbers = [1, 2, 3, 4, 5]
my_list = numbers[1:3]
print(my_list)

numbers = [1, 2, 3, 4, 5]
my_list = numbers[:-1]
print(my_list)

numbers = [1, 2, 3, 4, 5]
my_list = numbers[:]
print(my_list)

names = ['Джим', 'Джилл', 'Джон', 'Джасмин']
if 'Джасмин' not in names:
    print ('Не могу найти Джасмин.')
else:
    print('Ceмья Джасмин: ', end='')
    print(names)