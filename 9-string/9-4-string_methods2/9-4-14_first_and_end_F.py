import os
clear = lambda: os.system('cls')
clear()

str = 'hello'
#str = input()
if str.count('f') > 1:
    print(str.index('f'), str.rindex('f'))  
elif str.count('f') == 1:
    print(str.index('f'))  
elif str.count('f') == 0:
    print("NO")
