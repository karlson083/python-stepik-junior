import os
from posixpath import split
clear = lambda: os.system('cls')
clear()

# объявление функции


def draw_triangle():
    for i in range(10):
        print('*' * (i+1))
    

# основная программа
draw_triangle()  # вызов функции

# объявление функции
def draw_triangle():
    print(*['*' * i for i in range(1, 11)], sep='\n')

# основная программа
draw_triangle()  # вызов функции