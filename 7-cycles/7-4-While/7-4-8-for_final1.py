import os
clear = lambda: os.system('cls')
clear()

text = ''
while text != 'КОНЕЦ':
    print(text)
    text = input()