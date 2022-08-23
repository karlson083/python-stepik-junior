import os
clear = lambda: os.system('cls')
clear()

#str = input()
str = 'nezabud dl-6'
c = 0
for i in str:
    if i in ('1','2','3','4','5','6','7','8','9','0'):
        c += 1
print(c)


n = input()
count = 0
for i in range(10):
    count += n.count(str(i))
print(count)