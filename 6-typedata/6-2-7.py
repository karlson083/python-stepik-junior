import os
clear = lambda: os.system('cls')
clear()

teamname = input()
colch = str(len(teamname))
textend = 'Футбольная команда ' + teamname + ' имеет длину ' + colch + ' символов'
print(textend)
