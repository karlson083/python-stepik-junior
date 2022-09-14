import os
from posixpath import split
clear = lambda: os.system('cls')
clear()



# объявление функции
def is_prime(num):
    cnt = 0
    for i in range(1,num+1):
        if num % i == 0:
            cnt += 1
    if cnt == 2:
        flag = True
    else:
        flag = False
    
    return flag
    

# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))





# объявление функции
def is_prime(num):
    return len([i for i in range(1, num+1) if num % i == 0]) == 2

# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))



# объявление функции
def is_prime(num):
    if num == 1:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

# считываем данные
n = int(input())

# вызываем функцию
print(is_prime(n))