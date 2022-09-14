import os
from posixpath import split
clear = lambda: os.system('cls')
clear()



# объявление функции
def quick_merge(list):
    list_out =[]
    for i in list:
        list_out += i
        list_out.sort()

    return list_out
    

# считываем данные

n = int(input())
numbers = []
for _ in range(n):
    numbers.append([int(c) for c in input().split()])


#numbers = [int(c) for c in input().split()]


# вызываем функцию
print(*(quick_merge(numbers)))