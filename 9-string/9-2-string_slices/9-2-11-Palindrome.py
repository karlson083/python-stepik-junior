import os
clear = lambda: os.system('cls')
clear()

s = input()
if s[::1] == s[::-1]:
    print("YES")
else:
    print("NO")


n = input()
print('YES' if n == n[::-1] else 'NO')


s = input()
if s[:] == s[::-1]:
    print('YES')
else:
    print('NO')