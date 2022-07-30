import os
clear = lambda: os.system('cls')
clear()

s = 'Hello'
n = len(s)  # значение переменной равно 5
print(n)

s = 'All you need is love'
if 'love' in s:
    print('❤️')
else:
    print('💔')


s = 'abcdef'
for i in range(len(s)):
    print(s[i])


s = 'abcdef'
for c in s:
    print(c)


s = 'abcdefg'
print(s[0] + s[2] + s[4] + s[6])

s = 'abcdefg'
print(s[0]*3 + s[-1]*3 + s[3]*2 + s[3]*2)

s = '01234567891011121314151617'
for i in range(0, len(s), 5):
    print(s[i], end='')