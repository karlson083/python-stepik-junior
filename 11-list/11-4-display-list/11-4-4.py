import os
clear = lambda: os.system('cls')
clear()


n = int(input())
numbers = []
for i in range(n):
    numbers.append(int(input()))
for i in range(n):
    if numbers[i] != min(numbers) and numbers[i] != max(numbers):
        print(numbers[i])
