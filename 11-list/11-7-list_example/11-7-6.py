import os
clear = lambda: os.system('cls')
clear()

palindromes = [i for i in range(100,1001) if str(i) == str(i)[::-1]]

print(palindromes)