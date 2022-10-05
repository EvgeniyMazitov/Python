# num = float(input('Введите число'))

# num = str(num)
# summa: int = 0
# for i in num:
#     print(i.isdigit())
#     if i.isdigit():
#         summa+-int(i)
# print(summa)


# import random

# list = []

# for _ in range(10):
#     list.append(random.randint(0, 50))
# print('Оригинальный список: ' + str(list))

# for i in range(len(list)-1):
#     j = random.randint(0, len(list)-1)
#     list[i], list[j] = list[j], list[i]

# print('Перемешенный список: ' + str(list))

from asyncore import write


path = r'Seminar2HomeWork\text.txt'
with open(path, 'r') as data:
    coef1 = data.readline()[:-1]
    coef2 = data.readline()

with open(path, 'w', encoding='UTF-8') as data:
    data.write('Привет')

    print(coef1, end=" ")
    print(coef2)
