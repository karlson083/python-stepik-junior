import os
clear = lambda: os.system('cls')
clear()

max = 0
num = int(input())
min = 9
while num != 0:
    last_digit = num % 10
    if last_digit > max:
        max = last_digit
    if last_digit < min:
        min = last_digit
    num = num // 10
print('Максимальная цифра равна', max)
print('Минимальная цифра равна', min)


n, x, m = int(input()), -1, 10
while n:
    x = max(x, n % 10)
    m = min(m, n % 10)
    n //= 10
print('Максимальная цифра равна', x)
print('Минимальная цифра равна', m)


x = str(input())
print('Максимальная цифра равна', max(x))
print('Минимальная цифра равна', min(x))