import os
from posixpath import split
clear = lambda: os.system('cls')
clear()



# объявление функции
def find_all(target, symbol):
    return [i for i in range(len(target)) if target[i].find(symbol) == 0]
        

# считываем данные
s = input()
char = input()

# вызываем функцию
print(find_all(s, char))