import os
clear = lambda: os.system('cls')
clear()


num = int(input())
last_digit = 0
while num != 0:
    second_digit = last_digit
    last_digit = num % 10
    num = num // 10
print(second_digit)


n = int(input())
while n > 99:
    n //= 10
print(n % 10)

n = int(input())
while n > 9:
    x = n % 10
    n = n // 10
print(x)