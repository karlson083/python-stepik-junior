import os
clear = lambda: os.system('cls')
clear()

a, b, c, d, i = int(input()), int(input()), int(input()), int(input()), int(input())

minimum = min(a, b, c, d, i)
maximum = max(a, b, c, d, i)

print("Наименьшее число =", minimum)
print("Наибольшее число =", maximum)


