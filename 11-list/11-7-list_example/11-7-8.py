import os
from posixpath import split
clear = lambda: os.system('cls')
clear()

text_line = input()
number_list = text_line.split()

number_list = [int(i) ** 3 for i in number_list]
print(number_list, sep = ' ')
