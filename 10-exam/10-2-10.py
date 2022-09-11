<<<<<<< HEAD
=======


>>>>>>> 11-4-display-list
import os
clear = lambda: os.system('cls')
clear()

str = 'abch12345h'
#str = input()
print(str[:str.index('h')+1], str[str.rindex('h')-1:str.index('h'):-1], str[str.rindex('h'):],sep = '')  



s=input()
a=int(s.find('h'))
b=int(s.rfind('h'))
print(s[:a]+s[b:a:-1]+s[b:])