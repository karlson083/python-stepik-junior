import os
clear = lambda: os.system('cls')
clear()

total = 0
for bik in range(1, 100):
    for korov in range(1, 100):
        for telen in range(1, 100):
            if 10 * bik + 5 * korov + 0.5 * telen == 100 and bik+korov+telen == 100:
                total += 1
                print('bik =', bik, 'korov =', korov, 'telen =', telen)
print('Общее количество натуральных решений =', total)