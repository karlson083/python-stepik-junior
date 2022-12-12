
import os
clear = lambda: os.system('cls')
clear()

text = 'Шсъцхр щмчжмщ йшм, нмтзж йшм лхшщзщг.'
diff = -7

if diff > 0:
    for i in text:
        if 1040 <= ord(i) <= 1072:
            print(chr(ord(i) + diff - 32) if ord(i) + diff > 1072 else (chr(ord(i) + diff) if 1040 <= ord(i) <= 1072 else i), end = '')
        elif 1073 <= ord(i) <= 1103:
            print(chr(ord(i) + diff - 32) if ord(i) + diff > 1103 else (chr(ord(i) + diff) if 1073 <= ord(i) <= 1103 else i), end = '')
        else:
            print(i, end = '')
elif diff < 0:
    for i in text:
        if 1040 <= ord(i) <= 1071:
            print(chr(ord(i) + diff + 32) if ord(i) + diff < 1040 else (chr(ord(i) + diff) if 1040 <= ord(i) <= 1071 else i), end = '')
        elif 1072 <= ord(i) <= 1103:
            print(chr(ord(i) + diff + 32) if ord(i) + diff < 1072 else (chr(ord(i) + diff) if 1072 <= ord(i) <= 1103 else i), end = '')
        else:
            print(i, end = '')
else:
    print('Смещени еравно нулю')
'''
for i in range(1040,1110):
    print(i, chr(i), end = ' ')
    '''
