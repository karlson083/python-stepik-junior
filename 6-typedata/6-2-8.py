import os
clear = lambda: os.system('cls')
clear()

city1 = input()
city2 = input()
city3 = input()
col1 = len(city1)
col2 = len(city2)
col3 = len(city3)
mincol = min(col1, col2, col3)
maxcol = max(col1, col2, col3)
if len(city1) == mincol:
    print(city1)
elif len(city2) == mincol:
    print(city2)
else:
    print(city3)
if len(city1) == maxcol:
    print(city1)
elif len(city2) == maxcol:
    print(city2)
else:
    print(city3)


    a, b, c = input(), input(), input()

if(len(a) < len(b)): b, a = a, b
if(len(c) > len(b)): c, b = b, c
if(len(c) > len(a)): c, a = a, c

print(c, a, sep='\n')