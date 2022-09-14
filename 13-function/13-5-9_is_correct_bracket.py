import os
from posixpath import split
clear = lambda: os.system('cls')
clear()


# объявление функции
def is_correct_bracket(text):
    cnt_bracket = 0
    for i in text:
        if i == '(':
            cnt_bracket += 1
        elif i == ')':
            cnt_bracket -= 1
        else:
            return 'Error input'
        if cnt_bracket < 0:
            return False
    if cnt_bracket == 0:
        return True
    else:
        return False

# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))





# объявление функции
def is_correct_bracket(text):
    while '()' in text:
        text = text.replace('()', '')
    return not text

# считываем данные
txt = input()

# вызываем функцию
print(is_correct_bracket(txt))