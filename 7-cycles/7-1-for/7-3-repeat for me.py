import os
clear = lambda: os.system('cls')
clear()

simple_text = str(input())
text_repeat = int(input())

for i in range(text_repeat):
    print(simple_text)