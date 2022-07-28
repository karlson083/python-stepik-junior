import os
clear = lambda: os.system('cls')
clear()

'''
n = int(input())
while n != 0:  # пока в числе есть цифры
    last_digit = n % 10  # получить последнюю цифру
    print(last_digit)# код обработки последней цифры
    n = n // 10  # удалить последнюю цифру из числа
'''

num = int(input())
has_seven = False  # сигнальная метка

while num != 0:
    last_digit = num % 10
    if last_digit == 7:
        has_seven = True
    num = num // 10

if has_seven == True:
    print('YES')
else:
    print('NO')