import os
clear = lambda: os.system('cls')
clear()


#s = input()
s = 'abcABCD12345'

s2 = s.upper()
count = 0
for i in range(len(s)):
    if s[i] != s2[i]:
        count += 1
print(count)

s, counter = input(), 0
for i in s:
    if i != i.upper():  # условие выполняется только для букв в нижнем регистре
        counter += 1
print(counter)