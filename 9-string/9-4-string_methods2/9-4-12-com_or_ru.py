import os
clear = lambda: os.system('cls')
clear()

str = 'www.google.com'
#str = input()
if str.endswith('.com') or str.endswith('.ru'):
    print("YES")
else:
    print("NO")



print('YES' if input().endswith(('.com','.ru')) else 'NO')