import os
from posixpath import split
clear = lambda: os.system('cls')
clear()

# объявление функции
def print_digit_sum(num):
    count = 0
    for i in range(len(num)):
        count += int(num[i])
    print(count)


# считываем данные
n = input()

# вызываем функцию
print_digit_sum(n)




def print_digit_sum(num):
    print(sum(int(i) for i in str(num)))

n = int(input())

print_digit_sum(n)