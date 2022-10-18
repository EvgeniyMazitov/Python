# <Задание 1>
# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# Пример:
# [2, 3, 5, 9, 3] => на нечётных позициях элементы 3 и 9, ответ: 12


def EnterIntNumber(question):
    number = 0
    while True:
        try:
            number = int(input(question))
            break
        except:
            print("Введеное значение не допустимо, попробуйте еще раз")
    return number


inputList = []
LenList = EnterIntNumber("Введите количество элементов в списке : ")

for i in range(0, LenList):
    inputList.append(EnterIntNumber(
        f'Введите значение {i+1}-го элемента списка : '))

print(f'Анализируемый список: {inputList}')

# sum = 0
# for i in range(1, len(inputList), 2):
#     sum += inputList[i]

result = sum([y for x, y in enumerate(inputList) if x % 2 != 0])

print(f'Сумма элементов на нечетных позициях списка = {result}')
# print(f'Сумма элементов на нечетных позициях списка = {sum}')
