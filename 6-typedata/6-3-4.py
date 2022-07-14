import os
from re import S
import sre_parse
from telnetlib import X3PAD
clear = lambda: os.system('cls')
clear()

from math import sqrt, pow
a, b = float(input()), float(input())
x1 = (a+b)/2
x2 = sqrt(a*b)
x3 = (2 * a * b) / (a + b)
x4 = sqrt((pow(a,2) + pow(b,2))/2)
print(x1)
print(x2)
print(x3)
print(x4)