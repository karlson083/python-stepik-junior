import os
from re import S
import sre_parse
from telnetlib import X3PAD
clear = lambda: os.system('cls')
clear()

from math import pow, sin, cos, tan, pi, radians
x = float(input())
r = radians(x)

xx = sin(r) + cos(r) + pow(tan(r), 2)
print(xx)