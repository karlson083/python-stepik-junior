import os
from re import S
import sre_parse
from telnetlib import X3PAD
clear = lambda: os.system('cls')
clear()

from math import ceil, floor
x = float(input())

xx = ceil(x) + floor(x)
print(xx)