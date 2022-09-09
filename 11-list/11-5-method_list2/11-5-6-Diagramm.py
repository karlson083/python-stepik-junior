import os
clear = lambda: os.system('cls')
clear()

s = '5 3 1 7 10 2'
#s = input()
digital_string = s.split()
for i in digital_string:
    print('+' * int(i))


for i in input().split():
    print('+' * int(i))