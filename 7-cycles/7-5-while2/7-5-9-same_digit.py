import os
clear = lambda: os.system('cls')
clear()


num = int(input())
text = 'YES'
while num > 9:
    last_digit1 = num % 10
    last_digit2 = (num // 10) % 10
    if last_digit1 != last_digit2:
        text = 'NO'
    num = num // 10
print(text)





x = input()
print('YES' if max(x) == min(x) else 'NO')




num = str(input())
max, min = max(num), min(num)
if max == min:
    print('YES')
else:
    print('NO')




    x = input()
if max(x) == min(x):
    print('YES')