import os
clear = lambda: os.system('cls')
clear()

dogyear = float(input())

if dogyear > 2:
    print( (dogyear - 2) * 4 + 2 * 10.5)
else:
    print ( dogyear * 10.5 )