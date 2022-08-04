import os
clear = lambda: os.system('cls')
clear()

#s = input()
s = 'АааГГЦЦцТТттт'
s = s.lower()
print('Аденин:', s.count('а'))
print('Гуанин:', s.count('г'))
print('Цитозин:', s.count('ц'))
print('Тимин:', s.count('т'))
