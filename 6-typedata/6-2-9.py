import os
clear = lambda: os.system('cls')
clear()

c1 = input()
c2 = input()
c3 = input()
col1 = len(c1)
col2 = len(c2)
col3 = len(c3)
mincol = min(col1, col2, col3)
maxcol = max(col1, col2, col3)
if col1 != mincol and col1 != maxcol:
    avercol = col1
elif col2 != mincol and col2 != maxcol:
    avercol = col2
else:
    avercol = col3

if maxcol - avercol == avercol - mincol:
    print("YES")
else:
    print("NO")