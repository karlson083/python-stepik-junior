import os
clear = lambda: os.system('cls')
clear()

text = ''
count = 0
while text not in ['стоп', 'хватит', 'достаточно']:
    text = input()
    if text not in ['стоп', 'хватит', 'достаточно']:
        count += 1
print(count)

#################

a = 0
while input() not in ("стоп", "хватит", "достаточно"):
    a+=1
print(a)

######################

a, k = input(), 0
while a not in ('стоп', 'хватит', 'достаточно'):
    k += 1
    a = input()
print(k)