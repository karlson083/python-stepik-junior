import os
clear = lambda: os.system('cls')
clear()

x = int(input())

a = x // 100
b = x // 10 % 10
c = x % 10
'''
print(a)
print(b)
print(c)
'''

minimum = min(a, b, c)
maximum = max(a, b, c)

if minimum < a < maximum:
    average = a
elif minimum < b < maximum:
    average = b
elif minimum < c < maximum:
    average = c
'''
print(maximum)
print(average)
print(minimum)
'''

raznost = maximum - minimum

if raznost == average:
    print("Число интересное")
else:
    print("Число неинтересное")