
import os,random
clear = lambda: os.system('cls')
clear()

word_list = ["вася", "петя",'ктото','колия']

def input_chairs():
    str0 = input('Введите слово или букву:-> ')
    while not str0.isalpha():
      str0 = input('Ввод должен содержать только буквы. Введите слово или букву:-> ')
    print('Вы ввели ', str0)
    return str0.upper()

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

def word_completion_change(str1_0,word_0,word_completion_0):
   for i in range(0,len(word_0)):
      if word_0[i] == str1_0:
         word_completion_0 = word_completion_0[:i] + str1_0 + word_completion_0[i+1:]
   return word_completion_0


def play(word):
    # тело функции
    word_completion = '-' * len(word)  # строка, содержащая символы _ на каждую букву задуманного слова
    guessed = False                    # сигнальная метка
    guessed_letters = []               # список уже названных букв
    guessed_words = []                 # список уже названных слов
    tries = 6                          # количество попыток
    print('Lets play')
    while not guessed: #Повторяющийся цикл попыток угадать
      clear()
      print(display_hangman(tries),' Осталось промахов - ',tries)
      print('Ваше слово выглядит так:->',word_completion,' подсказка ', word)
      str1 = input_chairs() # Вызов функции ввода слова или буквы с проркой ввода
      if str1 in guessed_letters or str1 in guessed_words: # Проверка на повторение ранее введенные слово или букву
         print('Вы ввели ранее введенное слово или букву, количество попыток не будет уменьшено. Повторите ввод')
      else: # введенный символ или слово ранее не вводились продолжаем проверку
         tries -= 1 # Отнимаем количество попыток
         if len(str1) == 1: # если введена одна буква обрабатываем ввод
      #      print('Проверка с одной буквой')
            guessed_letters.append(str1) # добавляем в список
            if word.count(str1) > 0: # Проверяем наличие введенной буквы
               word_completion = word_completion_change(str1,word,word_completion) # Вызываем процедуру по изминению черточек на букву
               if word_completion == word: # Проверяем слово на разгаданность
                  print('Вы разгадали слово по буквам, ваше слово -> ', word_completion)
                  guessed = True
            else:
               print('Нет данной буквы в загаданном слове')
         else:
      #     print('Проверка со словом')
            guessed_words.append(str1)
            if str1 == word:
               print('Вы разгадали слово целиком -> ', str1)
               guessed = True           
            else:
               print('Вы не угадали слово, пробуйте дальше')
      if not tries and not guessed:
         clear()
         print(display_hangman(tries),'Это была ваша последняя попытка')
         print('Вы не угадали слово за отведенные вам попытки. Вы проиграли. Раунд окончен. Верное слово было ', word)
         guessed = True

    pass


playgame = True
while playgame:
   play(get_word(word_list))
   answer = str(input('Введите Да, Yes, True 1 или нажмите Enter для повтора игры. Любой другой ввод закончит работу иргы ')).lower()
   ok_answers = ['да', 'yes', 'true', '1', '']
   if answer not in ok_answers:
      playgame = False
