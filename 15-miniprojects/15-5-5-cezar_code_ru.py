
import os
clear = lambda: os.system('cls')
clear()

text = 'Блажен, кто верует, тепло ему на свете!'
diff = 10

for i in text:
    print(chr(ord(i) + diff -32) if ord(i) + diff >= 1103 else (chr(ord(i) + diff) if 1040 <= ord(i) <= 1103 else i), end = '')

'''
for i in range(1040,1104):
    print(i, chr(i), end = ' ')
    '''
