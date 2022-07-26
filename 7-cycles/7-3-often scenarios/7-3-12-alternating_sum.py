import os
clear = lambda: os.system('cls')
clear()

result = 0
n = int(input())
for i in range(1, n + 1):
    minus_one = -1
    degree_sum = i + 1
    result += minus_one ** degree_sum * i
print(result)
