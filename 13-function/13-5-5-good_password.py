import os
from posixpath import split
clear = lambda: os.system('cls')
clear()


# объявление функции
def is_password_good(password):
    if len(password) < 8:
        return False
    elif len([i for i in password if i.isupper()]) == 0:
        return False
    elif len([i for i in password if i.islower()]) == 0:
        return False
    elif len([i for i in password if i.isdigit()]) == 0:
        return False
    else:
        return True    
    
    
# считываем данные
txt = input()

# вызываем функцию
print(is_password_good(txt))