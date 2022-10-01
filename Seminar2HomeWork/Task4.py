# Реализуйте алгоритм перемешивания списка, без использования встроеных методов (особенно SHUFFLE, без него) можно (нужно) использовать библиотеку Random

import random


def EnterIntNumber(question):
    number = 0
    while True:
        try:
            number = int(input(question))
            break
        except:
            print("Введеное значение не допустимо, попробуйте еще раз")
    return number


def InputSpisok(numberN):
    for i in range(0, numberN):
        list.append(input(f'Введите {i+1}-й элемент списка: '))


def ShuffleSpisok(list, nShuffle):
    for i in range(0, nShuffle):
        random1 = random.randint(0, len(list)-1)
        random2 = random.randint(0, len(list)-1)
        buff = list[random2]
        list[random2] = list[random1]
        list[random1] = buff
    return list


numberN = EnterIntNumber("Введите число элементов списка N: ")
nShuffle = EnterIntNumber("Введите число паеремешиваний списка K: ")

list = []

InputSpisok(numberN)
print('Исходный список:')
print(list)

ShuffleSpisok(list, nShuffle)
print('Перемешанный список:')
print(list)
