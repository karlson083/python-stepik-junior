import os
clear = lambda: os.system('cls')
clear()


num = int(input())
for i in range(2, num+1):
    if num % i == 0:
        min_divisor = i
        break
print(min_divisor)
    
