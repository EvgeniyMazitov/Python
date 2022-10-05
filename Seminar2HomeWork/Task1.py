# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.
# НЕОБЯЗАТЕЛЬНО Попробовать решить не переводя числа в строку
# Пример:
# 6782 -> 23
# 0,56 -> 11

def EnterFloat(question):
    number = 0
    while True:
        try:
            number = float(input(question))
            break
        except:
            print("Введеное значение не допустимо, попробуйте еще раз")
    return number


def DigitSum(number):
    sumOfDigit = 0
    while number != 0:
        sumOfDigit += number % 10
        number = int(number/10)
    return sumOfDigit


rounded = 2
inputNumber = EnterFloat("Введите вещественное число: ")
buffer = inputNumber

while (int(buffer) / float(buffer)) != 1:
    buffer = round(buffer*10, rounded)

intBuffer = int(buffer)
print(intBuffer)

print(
    f'Сумма всех цифр числа {inputNumber} с точностью не более {rounded} знаков после запятой равна {DigitSum(int(buffer))}')
