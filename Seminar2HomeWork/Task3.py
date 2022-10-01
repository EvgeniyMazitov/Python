# Задайте список из n чисел последовательности (1+1/n)^n
# Выведите на экран саму последовательность и сумму элементов этой последовательности (для проверки сумма для 4 элементов = 9,06 (примерно)

def EnterIntNumber(question):
    number = 0
    while True:
        try:
            number = int(input(question))
            break
        except:
            print("Введеное значение не допустимо, попробуйте еще раз")
    return number


numberN = EnterIntNumber("Введите число N: ")

list = []
for i in range(1, numberN+1):
    list.append(round(pow((1+(1/i)), i), 2))
print(f'Последовательность (1+1/n) ^ n для числа членов {numberN}:')
print(list)
result = 0
for i in list:
    result += i
print(f'Сумма {numberN} чисел последовательности = {result}')
