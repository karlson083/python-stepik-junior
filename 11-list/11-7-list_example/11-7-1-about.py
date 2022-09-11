import os
clear = lambda: os.system('cls')
clear()

zeros = [0 for i in range(10)]
print(zeros)

squares = [i ** 2 for i in range(10)]
print(squares)

cubes = [i ** 3 for i in range(10, 21)]
print(cubes)

chars = [c for c in 'abcdefg']
print(chars)


numbers = [i * j for i in range(1, 5) for j in range(2)]
print(numbers)