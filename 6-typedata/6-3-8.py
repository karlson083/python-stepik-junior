import os
from telnetlib import X3PAD
clear = lambda: os.system('cls')
clear()
from math import *

n = float(input())
a = float(input())

s = (n * a**2)/(4*tan(pi/n))
print(s)


