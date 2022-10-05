# Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.

# def EnterInt(question):
#     number = 0
#     while True:
#         try:
#             number = int(input(question))
#             break
#         except:
#             print("Введеное значение не допустимо, попробуйте еще раз")
#     return number


g = ['qweqweeqwrqw', 'qweqweqweaf', '1242353sdafsdf',
     '0987567432yhnvcxcv', '2314trehnxb']

# numberN = EnterInt("Введите число: ")

# list = []

# flag = False

# for i in g:
#     for j in i:
#         flag = False
#         if j == str(numberN):
#             flag == True
#         list.append(flag)

# print(list)

numberN = input("Введите число: ")

flag = True

for i in g:
    for j in i:
        if numberN == j:
            print("Число присутствует в элементе " + i)
            flag = False
            break
if flag:
    print("Число не найдено!")


# result = []
# for item in g:
#     f = item.find(str(numberN))
#     if f >= 0:
#         result.append('true')
#     else:
#         result.append('false')

# print(g)
# print(result)
