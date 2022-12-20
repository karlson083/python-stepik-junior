
import os
clear = lambda: os.system('cls')
clear()

text = 'Sgd fqzrr hr zkvzxr fqddmdq nm sgd nsgdq rhcd ne sgd edmbd.'
#diff = -25
text_list = text.split()


def decode(text,diff):
    if diff > 0:
        for i in text:
            if 65 <= ord(i) <= 91:
                print(chr(ord(i) + diff - 26) if ord(i) + diff > 91 else (chr(ord(i) + diff) if 65 <= ord(i) <= 91 else i), end = '')
            elif 97 <= ord(i) <= 122:
                print(chr(ord(i) + diff - 26) if ord(i) + diff > 122 else (chr(ord(i) + diff) if 97 <= ord(i) <= 122 else i), end = '')
            else:
                print(i, end = '')
    elif diff < 0:
        for i in text:
            if 65 <= ord(i) <= 91:
                print(chr(ord(i) + diff + 26) if ord(i) + diff < 65 else (chr(ord(i) + diff) if 65 <= ord(i) <= 91 else i), end = '')
            elif 97 <= ord(i) <= 122:
                print(chr(ord(i) + diff + 26) if ord(i) + diff < 97 else (chr(ord(i) + diff) if 97 <= ord(i) <= 122 else i), end = '')
            else:
                print(i, end = '')
    else:
        print(text)
pass

for i in text_list:
    decode(i,len(i))
    print(' ',end ='')




'''
for i in range(65,123):
    print(i, chr(i), end = ' ')
    
'''