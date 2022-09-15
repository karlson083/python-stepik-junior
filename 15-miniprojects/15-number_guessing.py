import random
import os
from posixpath import split
clear = lambda: os.system('cls')
clear()



rndx = random.randint(1,100)
print('Добро пожаловать в числовую угадайку')

def is_valid(check_x):
    return check_x.isdigit() and 1 <= int(check_x) <= 100 

def input_x():
    return input('Введите число от 1 до 100 - ')

x = input_x()

while not is_valid(x):
    print('А может быть все-таки введем целое число от 1 до 100?')
    x = input_x()

