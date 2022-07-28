import os
clear = lambda: os.system('cls')
clear()


num = int(input())
text = 'YES'
while num > 9:
    last_digit1 = num % 10
    last_digit2 = (num // 10) % 10
    if last_digit1 > last_digit2:
        text = 'NO'
    num = num // 10
print(text)





n = int(input())
while n % 10 <= n // 10 % 10:
    n //= 10
print('YES' if n < 10 else 'NO')