import os
clear = lambda: os.system('cls')
clear()

# объявление функции
def get_shipping_cost(quantity):
    cost = 1000 + 120 * (quantity - 1)
    return cost
    
    
# считываем данные
n = int(input())

# вызываем функцию
print(get_shipping_cost(n))