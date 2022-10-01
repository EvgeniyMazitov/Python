# Напишите программу, которая принимает на вход число N и выдает набор произведений чисел от 1 до N.
# Пример:
# пусть N = 4, тогда (1, 1*2, 1*2*3, 1*2*3*4)

def EnterInt(question):
    number = 0
    while True:
        try:
            number = int(input(question))
            break
        except:
            print("Введеное значение не допустимо, попробуйте еще раз")
    return number

# # На всякий случай вариант с расчетом всех значений факториала от 1 до N и вывод результата умножения, а не строки со знаками

# def factorial(number):
#     if number == 1:
#         return 1
#     else:
#         return number * factorial(number-1)


# numberN = EnterInt("Введите число N: ")
# list = []
# for i in range(1, numberN+1):
#     list.append(factorial(i))
# print(list)


# Вывод как в задании
numberN = EnterInt("Введите число N: ")
list = []
for i in range(1, numberN+1):
    inputString = ""
    for j in range(1, i+1):
        inputString += str(j)
        if j < i:
            inputString += "*"
    list.append(inputString)

print(list)
