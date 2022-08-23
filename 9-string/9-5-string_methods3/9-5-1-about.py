from audioop import mul
import os
clear = lambda: os.system('cls')
clear()

s = 'aabbAA111ccDDaa'
print(s.isalnum())
print(s.isalpha())
print(s.isdigit())

s = 'aabb!@#$11cc'
print(s.islower())

s = 'AAb!@#$11CC'
print(s.isupper())

s = '    abbc    '
print(s.isspace())