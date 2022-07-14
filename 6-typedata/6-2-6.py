import os
clear = lambda: os.system('cls')
clear()

fn = input("First name ")
sn = input('Surname ')
textend = 'Hello ' + fn + ' ' + sn + '! You just delved into Python'
print(textend)
