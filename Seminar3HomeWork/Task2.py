# <Задание 2>
# Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# Пример:
# [2, 3, 4, 5, 6] => [12, 15, 16]
# [2, 3, 5, 6] => [12, 15]

def EnterIntNumber(question):
    number = 0
    while True:
        try:
            number = int(input(question))
            break
        except:
            print("Введеное значение не допустимо, попробуйте еще раз")
    return number


def MultiElements(list):
    resultList = []
    for i in range(0, round(len(list)/2)):
        resultList.append(list[i]*list[-i-1])
    if len(list) % 2 == 1:
        resultList.append(list[round(len(list)/2)]**2)
    return resultList


list = []
resultList = []
LenList = EnterIntNumber("Введите количество элементов в списке : ")

for i in range(0, LenList):
    list.append(EnterIntNumber(
        f'Введите значение {i+1}-го элемента списка : '))

print(f'Анализируемый список: {list}')
print(f'Сумма произведений пар чисел списка = {MultiElements(list)}')
