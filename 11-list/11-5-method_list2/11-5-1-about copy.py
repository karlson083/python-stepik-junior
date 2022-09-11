import os
clear = lambda: os.system('cls')
clear()

s = 'Python is the most powerful language'
words = s.split()
print(words)

'''
numbers = input().split()
for i in range(len(numbers)):
    numbers[i] = int(numbers[i])
'''

ip = '192.168.1.24'
numbers = ip.split('.')    # указываем явно разделитель
print(numbers)


words = ['Python', 'is', 'the', 'most', 'powerful', 'language']
s = ' '.join(words)
print(s)

words = ['Мы', 'учим', 'язык', 'Python']
print('*'.join(words))
print('-'.join(words))
print('?'.join(words))
print('!'.join(words))
print('*****'.join(words))
print('abc'.join(words))
print('123'.join(words))

s = 'BEEGEEK'
chars = list(s)
s = '**'.join(chars)
print(s)