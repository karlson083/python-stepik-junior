import os
clear = lambda: os.system('cls')
clear()

s = '192.168.0.3'
ip_bad = 0
#s = input()
digital_string = s.split('.')
for i in digital_string:
    if int(i) > 254 or int(i) < 0:
        ip_bad = 1
if ip_bad == 1:
    print('НЕТ')
else:
    print('ДА')

   

flag = 'ДА'
for c in input().split('.'):
    if int(c) > 255:
        flag = 'НЕТ'
print(flag)