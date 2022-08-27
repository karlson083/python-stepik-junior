import os
clear = lambda: os.system('cls')
clear()

str = 'jfnmdbsdfnsjfqenfdssjdfhsdjlkppppppppppppppppppgggggxxzzzssswwwwwwwwwwwwwwwwwwfgdfxdfg'
#str = input()
max_count = 0
max_char = ''

for i in str:
    if str.count(i) >= max_count:
        max_count = str.count(i)
        max_char = i
print(max_char)