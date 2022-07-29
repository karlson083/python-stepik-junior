from msvcrt import kbhit
import os
clear = lambda: os.system('cls')
clear()

n = int(input())
count1 = 0
count2 = 0
count3 = 0
while n != 0:
    count1 += n % 10
    n //= 10
while count1 != 0:
    count2 += count1 % 10
    count1 //=10
while count2 != 0:
    count3 += count2 % 10
    count2 //=10
print(count3)



number = int(input())

total = 0

while number > 9:  
    while number != 0:
        total += number % 10
        number //= 10
    number, total = total, 0

print(number)