import os
from re import S
clear = lambda: os.system('cls')
clear()

from math import *
R = float(input())
S = pi * pow(R,2)
C = 2 * pi * R
print(S)
print(C)