import os
from posixpath import split
clear = lambda: os.system('cls')
clear()

# объявление функции


def draw_line():
    print('**********')

def draw_start_end():
    print('*        *')

def draw_box():
    draw_line()
    for _ in range(12):
        draw_start_end()
    draw_line()

# основная программа
draw_box()  # вызов функции