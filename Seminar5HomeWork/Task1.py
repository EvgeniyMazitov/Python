# 1. Напишите программу, удаляющую из текста все слова, содержащие ""абв"".

inputStr = 'Кто-то забвение куда-то шел и абв был не так уж и порабв'
subString = 'абв'
print('Исходная строка:')
print(f'{inputStr}\n')
print('Слова исключаются по подстроке:')
print(f'{subString}\n')
words = inputStr.split(' ')
newWords = []
for i in words:
    if subString not in i:
        newWords.append(i)
newStr = ' '.join(newWords)
print('Результирующая строка:')
print(newStr)
