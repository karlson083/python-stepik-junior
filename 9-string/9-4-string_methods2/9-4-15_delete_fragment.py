import os
clear = lambda: os.system('cls')
clear()

str = 'In the hole in the ground there lived a hobbit'
#str = input()

print(str[:str.index('h')], str[str.rindex('h')+1:],sep = '')  
