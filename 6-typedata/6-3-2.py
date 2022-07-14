import os
clear = lambda: os.system('cls')
clear()

import math
x1, y1, x2, y2 = float(input()), float(input()), float(input()), float(input())
p = math.sqrt(math.pow((x1-x2),2) + math.pow((y1-y2),2))
print(p)
