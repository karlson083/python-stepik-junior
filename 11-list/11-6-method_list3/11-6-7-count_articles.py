import os
clear = lambda: os.system('cls')
clear()

text = 'William Shakespeare was born in the town of Stratford, England, in the year 1564. When he was a young man, Shakespeare moved to the city of London, where he began writing plays. His plays were soon very successful, and were enjoyed both by the common people of London and also by the rich and famous. In addition to his plays, Shakespeare wrote many short poems and a few longer poems. Like his plays, these poems are still famous today.'
#text = input()
text_list = text.split()
count = text_list.count('An')
count += text_list.count('an')
count += text_list.count('The')
count += text_list.count('the')
count += text_list.count('A')
count += text_list.count('a')
print('Общее количество артиклей:',count)


sp = input().lower().split()
a = sp.count("a") + sp.count("an") + sp.count("the")
print("Общее количество артиклей:", a)