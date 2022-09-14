import os
from posixpath import split
clear = lambda: os.system('cls')
clear()



# объявление функции
def get_next_prime(num):
    
    for j in range(num+1, 201):
        cnt = 0
        for i in range(1,j+1):
            if j % i == 0:
                cnt += 1
        if cnt == 2:
            return j
        
 
# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))



# объявление функции
def get_next_prime(num):
    num += 1
    for i in range(2, num):
        if num % i == 0:
            return get_next_prime(num)
    return num

# считываем данные
n = int(input())

# вызываем функцию
print(get_next_prime(n))