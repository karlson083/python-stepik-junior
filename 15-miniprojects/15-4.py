import random
import os
clear = lambda: os.system('cls')
clear()
#Объявляем константы и переменные
DIGITS = '0123456789'
LOWER_CASE_LETTERS = 'abcdefghijklmnopqrstuvwxyz'
UPPER_CASE_LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
PUNCTUATION = '!#$%&*+-=?@^_.'
BAD_CHAIRS = 'il1Lo0O'
chars = ''

#Вводим параметры по запросам
count_passwors = int(input('Введите количество паролей для генерации: '))
lenth_password = int(input('Введите длину одного пароля: '))
is_digit = bool(int(input('Включать ли цифры 0123456789? True,False,1,0: ')))
is_upper_leeters = bool(int(input('Включать ли прописные буквы ABCDEFGHIJKLMNOPQRSTUVWXYZ? 1,0: ')))
is_lower_letters = bool(int(input('Включать ли строчные буквы abcdefghijklmnopqrstuvwxyz? 1,0: ')))
is_punctuation = bool(int(input('Включать ли символы !#$%&*+-=?@^_? 1,0: ')))
is_on_bad_chairs = bool(int(input('Исключать ли неоднозначные символы il1Lo0O? 1,0: ')))

print(is_digit,is_upper_leeters,is_lower_letters,is_punctuation,is_on_bad_chairs)

if is_digit:
    chars += DIGITS
if is_upper_leeters:
    chars += UPPER_CASE_LETTERS
if is_lower_letters:
    chars += LOWER_CASE_LETTERS
if is_punctuation:
    chars += PUNCTUATION
if is_on_bad_chairs:
    for i in BAD_CHAIRS:
        if chars.find(i) != -1:
            chars = chars[:chars.find(i)] + chars[chars.find(i)+1:]
print(chars)

def generate_password(lenthf,chairsf):
    pass_out = ''
    for _ in range(lenthf):
        pass_out += chairsf[random.randint(0,len(chairsf)-1)]
    return pass_out
    
for _ in range(count_passwors):
    print(generate_password(lenth_password,chars))