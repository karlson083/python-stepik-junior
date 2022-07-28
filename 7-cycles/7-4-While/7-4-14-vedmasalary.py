
import os
clear = lambda: os.system('cls')
clear()

count = 0
x = int(input())
while x != 0:
    if x // 25 != 0:
        count += x // 25
        x -= ((x // 25) * 25)
    elif x // 10 != 0:
        count += x // 10
        x -= ((x // 10) * 10)
    elif x // 5 != 0:
        count += x // 5
        x -= ((x // 5) * 5)
    elif x // 1 != 0:
        count += x // 1
        x -= ((x // 1) * 1)
print(count)


n = int(input())
k = 0
for i in (25, 10, 5, 1):
    while n // i > 0:
        k += 1
        n -= i
print(k)

n = int(input())
total = n//25 + (n%25)//10 +((n%25)%10)//5 +(((n%25)%10)%5)
print(total)