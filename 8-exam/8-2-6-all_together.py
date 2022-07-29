from audioop import mul
import os
clear = lambda: os.system('cls')
clear()


x = 0
count_last_digit = 0
count = 0
n = int(input())
last_digit = n % 10
ok_digit = 0
sum_over_five = 0
multi_over_seven = 1
count_zero_five = 0
while n > 0:
    x = n % 10
    if x == 3:
        count += 1
    if x == last_digit:
        count_last_digit += 1
    if x %2 == 0:
        ok_digit += 1
    if x > 5:
        sum_over_five += x
    if x > 7:
        multi_over_seven *= x
    if x in {0,5}:
        count_zero_five += 1
    n //= 10
print(count)
print(count_last_digit)
print(ok_digit)
print(sum_over_five)
print(multi_over_seven)
print(count_zero_five)


n = int(input())
d3, d0d5, last_d, last_d_count = 0, 0, n % 10, 0
sum_over_5, mul_over_7, chetn = 0, 1, 0
while n > 0:
    d3 += n % 10 == 3
    d0d5 += n % 10 == 0 or n % 10 == 5
    last_d_count += n % 10 == last_d
    chetn += (n % 10) % 2 == 0
    if n % 10 > 5:
        sum_over_5 += n % 10
    if n % 10 > 7:
        mul_over_7 *= n % 10
    n //= 10
print(d3, last_d_count, chetn, sum_over_5, mul_over_7, d0d5, sep='\n')