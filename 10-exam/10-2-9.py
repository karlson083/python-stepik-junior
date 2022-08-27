from audioop import mul
import os
clear = lambda: os.system('cls')
clear()

str = 'python'
#str = input()
if str.count('f') > 1:
    print(str.index('f', str.index('f') + 1, len(str)))
elif str.count('f') == 1:
    print('-1')  
elif str.count('f') == 0:
    print("-2")
