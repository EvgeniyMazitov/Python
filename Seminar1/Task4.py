# 2. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.

#     *Примеры:*

#     - 6,78 -> 7
#     - 5 -> нет
#     - 0,34 -> 3
# 0,5 -> 5
# 45,098 -> 0

# from math import floor


# a = float(input('Введите дробное число: '))
# a = a*10
# result = floor(a % 10)
# print(result)


# number = float(input('Введите вещественное число: '))
# if int(number)/float(number) == 1.0:
#     print('Число целое')
# else:
#     print(int((number*10) % 10))


number = float(input('Введите вещественное число: '))
if number == int(number):
    print('Число целое')
else:
    print(int((number*10) % 10))
