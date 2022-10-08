
import os
clear = lambda: os.system('cls')
clear()

# объявление функции
def get_month(language, number):
    eng_month = ['january','february','march','april','may','june','july','august','september','october','november','december']
    rus_month = ['январь','февраль','март','апрель','май','июнь','июль','август','сентябрь','октябрь','ноябрь','декабрь']
    if language == 'en':
        return eng_month[number-1]
    else:
        return rus_month[number-1]
    
    
    
    
# считываем данные
lan = input()
num = int(input())

# вызываем функцию
print(get_month(lan, num))