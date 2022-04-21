import os
clear = lambda: os.system('cls')
clear()

num = 17
a = num % 10
b = num // 10
print(a)
print(b)

print("----------------")

num = 754
a = num % 10
b = (num % 100) // 10
c = num // 100
print(a)
print(b)
print(c)

print("----------------")

"""
Алгоритм получения цифр nn-значного числа
Несложно понять, по какому алгоритму можно найти каждую цифру nn-значного числа num:

Последняя цифра: (num % 101) // 100;
Предпоследняя цифра: (num % 102) // 101;
Предпредпоследняя цифра: (num % 103) // 102;
.....
Вторая цифра: (num % 10n-1) // 10n-2;
Первая цифра: (num % 10n) // 10n-1.
"""


"""
num = int(input())
last_digit = num % 10
first_digit = num // 10
print('Число десятков =', first_digit)
print('Число единиц =', last_digit)
"""
print("----------------")


"""
num = int(input())
last_digit = num % 10
first_digit = num // 10
print('Сумма цифр =', last_digit + first_digit)
"""

print("----------------")

"""
num = int(input())
digit3 = num % 10
digit2 = (num // 10) % 10
digit1 = num // 100
print(digit1, digit2, digit3, sep=',')

"""
print("----------------")

num = int(input())

a = num // 1000
b = (num % 1000) // 100
c = (num % 100) // 10
d = num % 10
#print(digit1, digit2, digit3, sep=',')


print("Цифра в позиции тысяч равна", a)
print("Цифра в позиции сотен равна", b)
print("Цифра в позиции десятков равна", c)
print("Цифра в позиции единиц равна", d)

a = 17 // (23 % 7)
b = 34 % a * 5 - 29 % 4 * 3
print(a * b)