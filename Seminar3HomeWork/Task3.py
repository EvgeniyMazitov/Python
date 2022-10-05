# <Задание 3>
# Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов. Если число целое, то его дробная часть не считается за 0 и оно (число) в сравнении не участвует

# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19


from gettext import find


def EnterFloat(question):
    number = 0
    while True:
        try:
            number = float(input(question))
            break
        except:
            print("Введеное значение не допустимо, попробуйте еще раз")
    return number


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
    list.append(EnterFloat(
        f'Введите значение {i+1}-го элемента списка : '))

print(f'Анализируемый список: {list}')

max = 0.0
min = 0.0
drobCh = 0
for i in range(0, len(list)):
    drobCh = str(list[i])[str(list[i]).find(".")+1:]
    if float("0."+drobCh) > max:
        max = float("0."+drobCh)
    if min == 0.0:
        min = float("0."+drobCh)
        print('flag')
    if float("0."+drobCh) < min and float("0."+drobCh) != 0.0:
        min = float("0."+drobCh)
print(
    f'Разница между максимальным и минимальным остатком исключая .0 = {max}-{min} = {max-min}')
