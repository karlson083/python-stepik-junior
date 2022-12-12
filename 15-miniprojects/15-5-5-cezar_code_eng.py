
import os
clear = lambda: os.system('cls')
clear()

text = 'To be, or not to be, that is the question!'
diff = 17
'''
for i in text:
    print(chr(ord(i) + diff -32) if ord(i) + diff >= 1103 else (chr(ord(i) + diff) if 1040 <= ord(i) <= 1103 else i), end = '')

'''
for i in range(65,123):
    print(i, chr(i), end = ' ')
    
