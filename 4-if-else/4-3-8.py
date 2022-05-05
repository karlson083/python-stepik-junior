import os
clear = lambda: os.system('cls')
clear()

color1 = input()
color2 = input()

if color1 == "красный" or color1 == "синий" or color1 == "желтый":
    if color2 == "красный" or color2 == "синий" or color2 == "желтый":
        if color1 == color2:
            print(color1)
        elif (color1 == "красный" and color2 == "синий") or (color2 == "красный" and color1 == "синий"):
            print("фиолетовый")
        elif (color1 == "красный" and color2 == "желтый") or (color2 == "красный" and color1 == "желтый"):
            print("оранжевый")
        elif (color1 == "синий" and color2 == "желтый") or (color2 == "синий" and color1 == "желтый"):
            print("зеленый")    
    else:
        print("ошибка цвета")    
else:
    print("ошибка цвета")