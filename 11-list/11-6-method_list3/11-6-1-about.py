import os
clear = lambda: os.system('cls')
clear()

names = ['Gvido', 'Roman' , 'Timur']
print(names)
names.insert(0, 'Anders')
print(names)
names.insert(3, 'Josef')
print(names)

names = ['Gvido', 'Roman' , 'Timur']
position = names.index('Timur')
print(position)

names = ['Gvido', 'Roman' , 'Timur']
if 'Anders' in names:
    position = names.index('Anders')
    print(position)
else:
    print('Такого значения нет в списке')

    food = ['Рис', 'Курица', 'Рыба', 'Брокколи', 'Рис']
print(food)
food.remove('Рис')
print(food)

names = ['Gvido', 'Roman' , 'Timur']
item = names.pop(1)
print(item)
print(names)

names = ['Timur', 'Gvido', 'Roman', 'Timur', 'Anders', 'Timur']
cnt1 = names.count('Timur')
cnt2 = names.count('Gvido')
cnt3 = names.count('Josef')

print(cnt1)
print(cnt2)
print(cnt3)

names = ['Gvido', 'Roman' , 'Timur']
names.reverse()
print(names)

names = ['Gvido', 'Roman' , 'Timur']
names.clear()
print(names)

colors = ['Orange']
colors.append('Red')
colors.append('Blue')
colors.append('Green')
colors.insert(0, 'Violet')
colors.insert(2, 'Purple')

print(colors)


colors = ['Red', 'Blue', 'Green', 'Black', 'White']
del colors[-1]
colors.remove('Green')

print(colors)


numbers = [4, 2, 8, 6, 5, 3, 10, 4, 100, 1, -7]
numbers.sort()
del numbers[0]
del numbers[-1]
numbers.sort(reverse=True)
print(numbers)