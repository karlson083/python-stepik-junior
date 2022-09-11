import os
from posixpath import split
clear = lambda: os.system('cls')
clear()

str_amount_tmp = '#12'
#str_amount_tmp = input()
str_amount = int(str_amount_tmp[1:])
text_list = []
tmp = ''
tmp2 = ''
for _ in range(str_amount):
    text_list.append(input())
for i in range(len(text_list)):
    tmp = text_list[i]
    if tmp.find('#') != -1:
        tmp2 = tmp[0:tmp.find('#')]
        text_list[i] = tmp2.rstrip()
print(*text_list, sep = '\n')



n = input()
for _ in range(int(n[1:])):
    s = input()
    if '#' in s:
        s = s[:s.find('#')]
    print(s.rstrip())