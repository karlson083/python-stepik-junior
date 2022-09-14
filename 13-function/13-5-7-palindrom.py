import os
from posixpath import split
clear = lambda: os.system('cls')
clear()


# объявление функции
def is_palindrome(text):
    
    txt_tmp = ''.join([i for i in text if i.isalpha()])
    if  txt_tmp.upper() == txt_tmp[::-1].upper():
        return True
    else:
        return False
    
# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))



# объявление функции
def is_palindrome(text):
    text = [i.lower() for i in text if i not in (',.!?- ')]
    return text == text[::-1]

# считываем данные
txt = input()

# вызываем функцию
print(is_palindrome(txt))