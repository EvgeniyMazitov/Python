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


list = []
LenList = EnterIntNumber("Введите количество элементов в списке : ")

for i in range(0, LenList):
    list.append(EnterIntNumber(
        f'Введите значение {i+1}-го элемента списка : '))

print(f'Анализируемый список: {list}')

sum = 0
for i in range(1, len(list)-1, 2):
    sum += list[i]
print(f'Сумма элементов на нечетных позициях списка = {sum}')
