# Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от -100 до 100)
# многочлена и записать в файл многочлен степени k
# k - максимальная степень многочлена, следующий степень на 1 меньше и так до ноля
# Коэффициенты расставляет random, поэтому при коэффициенте 0 просто пропускаем данную итерацию степени

# Пример:
# k=2 -> 2x² + 4x + 5 = 0 или x² + 5 = 0 или 10x² = 0
# k=5 -> 3x⁵ + 5x⁴ - 6x³ - 3x = 0

import random
import math


def EnterInt(question):
    number = 0
    while True:
        try:
            number = int(input(question))
            if number < 1:
                print("Введеное значение не допустимо, попробуйте еще раз")
                continue
            break
        except:
            print("Введеное значение не допустимо, попробуйте еще раз")
    return number


numberK = EnterInt('Введите натуральное число степени многочлена K: ')
path = 'Seminar4Homework/Mnogochlen.txt'
resultString = ""
for i in range(numberK, 0, -1):
    koeff = random.randint(-100, 101)
    if koeff != 0 and i == numberK:
        resultString += str(koeff) + "*x^"+str(i)
    elif koeff > 0 and i != 1:
        resultString += " + "+str(koeff) + "*x^"+str(i)
    elif koeff < 0 and i != 1:
        resultString += " - "+str(abs(koeff)) + "*x^"+str(i)
    elif koeff > 0 and i == 1:
        resultString += " + "+str(koeff)
    elif koeff < 0 and i == 1:
        resultString += " - "+str(abs(koeff))
resultString += " = 0"
print(resultString)

with open(path, 'a', encoding='UTF-8') as data:
    data.write(resultString)
