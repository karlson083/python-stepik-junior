import os
from posixpath import split
clear = lambda: os.system('cls')
clear()

def draw_box():
    for _ in range(5):
        print('*' * 7)

draw_box()