import random
import os
from posixpath import split
clear = lambda: os.system('cls')
clear()


print('Добро пожаловать в числовую угадайку')

def rnd_gen():
    max_gen_in = int(input('Введите целое число больше 1 для задания верхнего предела генерации числа '))
    while max_gen_in < 1:
        print('Вы ввеели число меньше или равное 1')
        max_gen_in = int(input('Введите целое число больше 1 для задания верхнего предела генерации числа '))
    rndx_in = random.randint(1,max_gen_in) # Задаем рандомом целочисленное значение которое нужно угадать
    print('Новое число которе нужно угадать сгенерировано в диапазоне от 1 до ', max_gen_in)
    print('Начинаем угадывать =)')
    return rndx_in , max_gen_in

rndx, max_gen = rnd_gen()

# Проверка на корретность введенного значения для угадывания
def is_valid(check_x,max_gen_in):
    return check_x.isdigit() and 1 <= int(check_x) <= max_gen_in 

#Ввод числа для угазывания пользователем
def input_x(max_gen_in):
    print('Введите число от 1 до', max_gen_in, '- ', end = '')
    return input()

#Основной цикл проверки правильности ввода
def general_input(max_gen_in):
    x = input_x(max_gen_in)
    while not is_valid(x,max_gen_in):
        print('А может быть все-таки введем целое число от 1 до', max_gen_in,'?')
        x = input_x(max_gen_in)
    return int(x)

count_try = 0
while 1:
    i = general_input(max_gen) 
    count_try += 1
    if i < rndx:
        print('Ваше число меньше загаданного, попробуйте еще разок')
    elif i > rndx:
        print('Ваше число больше загаданного, попробуйте еще разок')
    elif i == rndx:
        print('Вы угадали, за',count_try,'попыток поздравляем!')
        answer = input('Хотите сыграть еще раз? да, нет.')
        while answer not in ['да', 'нет']:
            print('Вы ввели неверно введите да или нет')
            answer = input('Хотите сыграть еще раз? да, нет.')
        if answer == 'да':
            clear()
            count_try = 0
            rndx, max_gen = rnd_gen()
        elif answer == 'нет':
            break
print('Спасибо, что играли в числовую угадайку. Еще увидимся...')





