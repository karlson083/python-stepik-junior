import os
clear = lambda: os.system('cls')
clear()


num = int(input())
last_num = num % 10
sum = 0
count = 0
multipy = 1
firts_num = 0

while num != 0:
    last_digit = num % 10
    sum += last_digit
    count += 1
    multipy *= last_digit
    firts_num = last_digit
    num = num // 10
print(sum)
print(count)
print(multipy)
print(sum / count)
print(firts_num)
print(firts_num + last_num)


n,sm,kol,pr = int(input()),0,0,1
np = n % 10
while n != 0:
    sm += n % 10 
    kol +=1
    pr *= n % 10
    n1 = n
    n = n // 10
print(sm,kol,pr,sm/kol,n1,n1+np,sep='\n')