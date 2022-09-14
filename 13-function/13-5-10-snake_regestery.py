import os
from posixpath import split
clear = lambda: os.system('cls')
clear()


# объявление функции
def convert_to_python_case(text):
    if text[0].isupper():
        text = text[0].lower() + text[1:]
    for i in text:
        if i.isupper():
            text = text.replace(i,'_' + i.lower())
    return text

# считываем данные
txt = input()

# вызываем функцию
print(convert_to_python_case(txt))


# put your python code here
def convert_to_python_case(text):
    s = ''
    for el in text:
        if el.isupper():
            s += '_'
        s += el.lower()
    return s[1:]
    

print(convert_to_python_case(input()))