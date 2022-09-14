import os
from posixpath import split
clear = lambda: os.system('cls')
clear()


# объявление функции
def is_palindrome(text):
       
    return text.upper() == text[::-1].upper()

def is_prime(num):
    return len([i for i in range(1, num+1) if num % i == 0]) == 2

def is_valid_password(password):
    pass_ls = password.split(':')
    if len(pass_ls) == 3:
        if not is_palindrome(str(pass_ls[0])):
            return False
        elif not is_prime(int(pass_ls[1])):
            return False
        elif int(pass_ls[2]) % 2 != 0:
            return False
        return True
    else:
        return False
    
   
# считываем данные
psw = input()

# вызываем функцию
print(is_valid_password(psw))