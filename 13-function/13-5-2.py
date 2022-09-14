import os
from posixpath import split
clear = lambda: os.system('cls')
clear()



def is_valid_triangle(a,b,c):
   
    if ( a + b > c ) and ( a + c > b ) and ( b + c > a ):
        return True
    else:
        return False

side1, side2, side3 = int(input()),int(input()),int(input())


print(is_valid_triangle(side1, side2, side3))

