
import os,random
clear = lambda: os.system('cls')
clear()

word_list = ["вася", "петя",'ктото','колия']

def input_chairs():
    str0 = input('Введите слово или букву')
    return str0

def get_word(wd_list): # функция получения рандомного слова
    return wd_list[random.randint(0,len(wd_list)-1)].upper()

def display_hangman(tries): # функция получения текущего состояния
    stages = [  # финальное состояние: голова, торс, обе руки, обе ноги
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / \\
                   -
                ''',
                # голова, торс, обе руки, одна нога
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |     / 
                   -
                ''',
                # голова, торс, обе руки
                '''
                   --------
                   |      |
                   |      O
                   |     \\|/
                   |      |
                   |      
                   -
                ''',
                # голова, торс и одна рука
                '''
                   --------
                   |      |
                   |      O
                   |     \\|
                   |      |
                   |     
                   -
                ''',
                # голова и торс
                '''
                   --------
                   |      |
                   |      O
                   |      |
                   |      |
                   |     
                   -
                ''',
                # голова
                '''
                   --------
                   |      |
                   |      O
                   |    
                   |      
                   |     
                   -
                ''',
                # начальное состояние
                '''
                   --------
                   |      |
                   |      
                   |    
                   |      
                   |     
                   -
                '''
    ]
    return stages[tries]

def play(word):
    # тело функции
    word_completion = '_' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False                    # сигнальная метка
    guessed_letters = []               # список уже названных букв
    guessed_words = []                 # список уже названных слов
    tries = 6                          # количество попыток
    print('Lets play')
    print(display_hangman(6),' Осталось промахов - ',tries)
    print(word_completion)
    str1 = input_chairs()
    if len(str1) != 1:
        print(str1)

    pass


"""
for _ in range(1,random.randint(1,100)):
    print(get_word(word_list))
    print(display_hangman(random.randint(0,6)))
"""