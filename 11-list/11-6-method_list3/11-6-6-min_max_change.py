import os
clear = lambda: os.system('cls')
clear()

numbers = '10 9 8 7 6 5 4 3 2 1'
numbers = input()
numbers_list = numbers.split()

for i in range(len(numbers_list)):
    numbers_list[i] = int(numbers_list[i])
print(numbers_list)
print(max(numbers_list))
min = min(numbers_list)
minid = numbers_list.index(min)
max = max(numbers_list)
maxid = numbers_list.index(max)
print(min,minid,max,maxid)
numbers_list[minid] = max
numbers_list[maxid] = min
print(*numbers_list, sep=' ')

