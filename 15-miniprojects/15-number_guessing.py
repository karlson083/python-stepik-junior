import random
import os
from posixpath import split
clear = lambda: os.system('cls')
clear()

rndx = random.randint(1,100) # Задаем рандомом целочисленное значение которое нужно угадать
print('Добро пожаловать в числовую угадайку')
#print(rndx)
# Проверка на корретность введенного значения для угадывания
def is_valid(check_x):
    return check_x.isdigit() and 1 <= int(check_x) <= 100 

#Ввод числа для угазывания пользователем
def input_x():
    return input('Введите число от 1 до 100 - ')

#Основной цикл проверки правильности ввода
def general_input():
    x = input_x()
    while not is_valid(x):
        print('А может быть все-таки введем целое число от 1 до 100?')
        x = input_x()
    return int(x)

count_try = 0
while 1:
    i = general_input() 
    count_try += 1
    if i < rndx:
        print('Ваше число меньше загаданного, попробуйте еще разок')
    elif i > rndx:
        print('Ваше число больше загаданного, попробуйте еще разок')
    elif i == rndx:
        print('Вы угадали, за',count_try,'попыток поздравляем!')
        break
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')





