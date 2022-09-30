# day = int(input('Введите число, обозначающее день недели [1-7]'))

# if 0 < day < 8:
#     if day == 6 or day == 7:
#         print("Это выходной")
#     else:
#         print("Это будний")
# else:
#     print("Такого дня недели нет")

# match day:
#     case 1:
#         print("Понедельник")
#     case 2:
#         print("Вторник")
#     case 3:
#         print("Среда")
#     case 4:
#         print("Четверг")
#     case 5:
#         print("пятница")
#     case 6:
#         print("суббота")
#     case 7:
#         print("Воскресенье")
#     case _:
#         print("Такого дня недели нет")

# for x in [True, False]:
#     for y in [True, False]:
#         for z in [True, False]:
#             if not (x or y or z) != (x and not y and not z):
#                 print("Не выполняется")
#                 break
# else:
#     print("Выполняется")


# number =0
# def enterInt():
#     while True:
#         try:
#             number=int(input("Введите целое число"))
#             break
#         except:
#             print("Введите целое число, попробуйте еще раз")
# num=enterInt()
# print(number)

# pointA=input("Введите X и Y через пробел").split(" ")
# pointB=input("Введите X и Y через пробел").split(" ")

# print(pointA)
# print(pointB)

# print(float((int(pointB[0])-int(pointA[0]))**2 + ((int(pointB[1])-int(pointA[1]))**2))


# n = int(input('Введите число: '))
# if (n % 5 == 0 and n % 10 == 0 or n % 15 == 0) and n % 30 != 0:
#     print("Выполняется")
# else:
#     print("Не выполняется")
