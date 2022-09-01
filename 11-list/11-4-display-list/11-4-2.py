import os
clear = lambda: os.system('cls')
clear()

numbers = [1, 78, 23, -65, 99, 9089, 34, -32, 0, -67, 1, 11, 111]

x = 0
for i in range(len(numbers)):
    x += numbers[i] ** 2 
print(x)
