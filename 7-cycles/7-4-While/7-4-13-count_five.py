import os
clear = lambda: os.system('cls')
clear()

count = 0
x = int(input())
while 1<= x <= 5:
    if x == 5:
        count += 1
    x = int(input())
print(count)


n, k = int(input()), 0
while 1 <= n <= 5:
    k += n == 5
    n = int(input())
print(k)