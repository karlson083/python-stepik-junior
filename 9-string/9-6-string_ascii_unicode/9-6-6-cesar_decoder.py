from audioop import mul
import os
clear = lambda: os.system('cls')
clear()

decoder_key = 25
coded_text = "jjjjjjj"
#decoder_key = int(input())
#coded_text = input()
for i in coded_text:
    if ord(i) - decoder_key < 97:
        print(chr(ord(i) - decoder_key+26), end = '')
    else:
        print(chr(ord(i) - decoder_key), end = '')

