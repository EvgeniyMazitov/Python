# вводим 2 числа с клавиатуры и находим НОК (наименьшее общее кратное), такое число которое бы делилась и на то, и на то без остатка (минимальное и делилось)

# numa = int(input('Введите a'))
# numb = int(input('Введите a'))
# number = max(numa, numb)
# print(numa, numb)
# while True:
#     if number % numa+number % numb == 0:
#         print(number)
#         break
#     number += 1


numA = int(input('Введите первое число: '))
numB = int(input('Введите второе число: '))

i = 1

while (min(numA, numB)*i) % max(numA, numB) != 0:
    i += 1

print(f'НОК чисел {numA} и {numB} равен {min(numA, numB)*i}')
