import os
clear = lambda: os.system('cls')
clear()

# объявление функции
def draw_triangle():
    a = 15
    h = 8
    for i in range(1,h+1):
        print(' ' * (h-i) + '*' * (15 - ((h-i)*2)))

# основная программа
draw_triangle()  # вызов функции