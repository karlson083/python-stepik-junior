import random
import os
from posixpath import split
clear = lambda: os.system('cls')
clear()


rnd = 0
rndx = random.randint(1,100000)
cnt = 0
while rnd != rndx:
    cnt += 1
    rnd = random.randint(1,100000)
    print(rnd, end = ' ')
print()
print(rndx, cnt)
