import os
clear = lambda: os.system('cls')
clear()

summ_glas = 0
summ_notglas = 0
#s = str(input())
s = 'Вдохновение – это умение приводить себя в рабочее состояние!'
for i in s:
    if i in ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'Ю', 'ё', 'е', 'Е']:
        summ_glas += 1
    if i in ['б', 'в', 'В', 'г', 'Г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'Н', 'п', 'р', 'с', 'С', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']:
        summ_notglas += 1
    #if i not in ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е','б', 'в', 'В', 'г', 'Г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'Н' 'п', 'р', 'с', 'С', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ']:
     #   print('bad', i)
print('Количество гласных букв равно', summ_glas)
print('Количество согласных букв равно', summ_notglas)
