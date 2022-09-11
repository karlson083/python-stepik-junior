import os
from posixpath import split
clear = lambda: os.system('cls')
clear()

s = input()
digit = '0123456789'
output_text = 'YES'
if len(s) == 12:
    for i in range(12):
        if  i in [0,1,2,4,5,6,8,9,10,11]:
            if s[i] not in digit:
                output_text="NO"
                break
        elif i in [3,7]:
            if s[i] !='-':
                output_text="NO"
                break
        else:
            print('YES')
elif len(s) == 14 and s[0] == '7':
    for i in range(14):
        if i in [0,2,3,4,6,7,8,10,11,12,13]:
            if s[i] not in digit:
                output_text="NO"
                break
        elif i in [1,5,9]:
            if s[i] !='-':
                output_text="NO"
                break
else:
    output_text="NO"
print(output_text)




n = input().split("-")
c = [len(i) for i in n] 
if c == [3, 3, 4] and ''.join(n).isdigit(): 
    print("YES")
elif c == [1, 3, 3, 4] and ''.join(n).isdigit() and n[0] == '7': 
    print("YES")
else:
    print("NO")