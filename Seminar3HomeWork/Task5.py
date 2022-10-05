# <Задание 5>
# Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.

# Пример:
# для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] (Негафибоначчи)

from tkinter import N


def EnterIntNumber(question):
    number = 0
    while True:
        try:
            number = int(input(question))
            break
        except:
            print("Введеное значение не допустимо, попробуйте еще раз")
    return number


numberN = EnterIntNumber("Введите число N(N>=0): ")

list = [1, 0, 1]
if numberN == 0:
    list = [0]
elif numberN == 1:
    list = [1, 0, 1]
elif numberN > 1:
    for i in range(2, numberN+1):
        list.append(list[i-1]+list[i])

    for i in range(0, -numberN+1, -1):
        list.insert(0, list[1]-list[0])
        print(list)
print(list)
