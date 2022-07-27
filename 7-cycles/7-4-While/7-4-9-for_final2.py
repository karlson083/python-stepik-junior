import os
clear = lambda: os.system('cls')
clear()

text = ''
while text not in ['КОНЕЦ', 'конец']:
    print(text)
    text = input()