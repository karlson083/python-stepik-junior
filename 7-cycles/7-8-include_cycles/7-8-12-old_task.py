import os
clear = lambda: os.system('cls')
clear()

total = 0
a = 1
b = 1
c = 1
d = 1
e = 1

for a in range(1, 151):
    if a ** 5 + b ** 5 + c ** 5 + d ** 5 == e ** 5:
        print(a + b + c + d + e)
        break
    for b in range(a, 151):
        if a ** 5 + b ** 5 + c ** 5 + d ** 5 == e ** 5:
            print(a + b + c + d + e)
            break
        for c in range(b, 151):
            if a ** 5 + b ** 5 + c ** 5 + d ** 5 == e ** 5:
                print(a + b + c + d + e)
                break
            for d in range(c, 151):
                if a ** 5 + b ** 5 + c ** 5 + d ** 5 == e ** 5:
                    print(a + b + c + d + e)
                    break
                for e in range(d, 151):
                    print(a,b,c,d,e)
                    # print(a ** 5, '+', b ** 5, '+', c ** 5, '+', d ** 5, '==', e ** 5)
                    #print(a ** 5 + b ** 5 + c ** 5 + d ** 5, '==', e ** 5, '     ', a ** 5, '+', b ** 5, '+', c ** 5, '+', d ** 5, '==', e ** 5)
                    if a ** 5 + b ** 5 + c ** 5 + d ** 5 == e ** 5:
                        print(a + b + c + d + e)
                        break