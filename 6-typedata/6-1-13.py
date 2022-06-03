import os
clear = lambda: os.system('cls')
clear()

a, b, c = int(input()), int(input()), int(input())

minimum = min(a, b, c)
maximum = max(a, b, c)

if minimum < a < maximum:
    average = a
elif minimum < b < maximum:
    average = b
elif minimum < c < maximum:
    average = c
elif a == b:
    average = a
elif c == a:
    average = c
elif b == c:
    average = b

print(maximum) 
print(average)  
print(minimum)  


#a, b, c = int(input()), int(input()), int(input())
print(max(a, b, c))
print(a + b + c - min(a, b, c) - max(a, b, c))
print(min(a, b, c))