import os
from posixpath import split
clear = lambda: os.system('cls')
clear()


# объявление функции
def is_one_away(word1, word2):
    if len(word1) == len(word2):
        cnt = 0
        for i in range(len(word1)):
            if word1[i] != word2[i]:
                cnt += 1
        if cnt == 1:
            return True
        else:
            return False
    else:
        return False
   
# считываем данные
txt1 = input()
txt2 = input()

# вызываем функцию
print(is_one_away(txt1, txt2))




# объявление функции
def is_one_away(word1, word2):
    return len([i for i in word1 if i not in word2]) == 1 and len(word1) == len(word2)

# считываем данные
txt1 = input()
txt2 = input()

# вызываем функцию
print(is_one_away(txt1, txt2))