
import os
clear = lambda: os.system('cls')
clear()


n = 10
#n = int(input())

print(bin(n).lstrip('0b'), oct(n).lstrip('0o'), hex(n).lstrip('0x').upper(), sep = '\n')