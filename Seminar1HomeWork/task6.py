# НЕОБЯЗАТЕЛЬНО
# Напишите программу, которая принимает на вход число и проверяет, кратно ли оно 5 и 10 или 15, но не 30.

inputDigit = int(input('Введите целое число для проверки кратности'))

if inputDigit == 0:
    print('Анализ не имеет смысла, т.к. введен 0')
elif (inputDigit % 5 == 0 or inputDigit % 10 == 0 or inputDigit % 15 == 0) and not inputDigit % 30 == 0:
    print(f'Число {inputDigit} кратно 5,10 или 15, но не кратно 30')
else:
    print(f'Число {inputDigit} не кратно 5,10 или 15 или кратно 30')
