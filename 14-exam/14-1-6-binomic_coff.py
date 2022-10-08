
import os
clear = lambda: os.system('cls')
clear()

# объявление функции

import math
def compute_binom(n, k):
    
    coff = math.factorial(n) / (math.factorial(k) * math.factorial(n-k))
    
    
    return int(coff)
    pass

# считываем данные
n = int(input())
k = int(input())

# вызываем функцию
print(compute_binom(n, k))