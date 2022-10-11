# 1


# def digit_after_dot_counter(num:float):
#     count = 0
#     div = 1
#     while True:
#         if not(num*div == int(num*div)):
#             count += 1
#             div *= 10
#         else: break
#     return count


# 2

# А такой вариант:
# while d * d <= n:
#         if n % d == 0:
#             Ans.append(d)
#             n //= d
#         else:
#             d += 1
#     if n > 1:
#         Ans.append(n)
#     return Ans


# def EnterInt(question):
#     number = 0
#     while True:
#         try:
#             number = int(input(question))
#             if number < 2:
#                 print("Введеное значение не допустимо, попробуйте еще раз")
#                 continue
#             break
#         except:
#             print("Введеное значение не допустимо, попробуйте еще раз")
#     return number


# numberN = EnterInt('Введите натуральное число N>=2: ')

# result = []
# minDel = 2
# bufferN = numberN

# while (minDel <= bufferN):
#     if bufferN % minDel == 0:
#         result.append(minDel)
#         bufferN /= minDel
#     else:
#         minDel += 1
# print(f'Список простых множителей числа {numberN}:')
# print(result)
# print(set(result))  # Вывод без дублей


# 4


# import random
# def createDict():
#     equation = {}
#     degree = int(input('Введите максимальную степень многочлена: '))
#     for i in range(degree, -1, -1):
#         equation[i] = random.randint(-10,10)
#     return equation

# def createEquation(equation: dict):
#     strEquation = ''
#     first = True

#     for k,v in equation.items():
#         if first:
#             first = False
#             if v > 0:
#                 strEquation += f'{v}*x^{k}'
#             elif v < 0:
#                 strEquation += f'-{abs(v)}*x^{k}'
#         else:
#             if v > 0:
#                 strEquation += f' + {v}*x^{k}'
#             elif v < 0:
#                 strEquation += f' - {abs(v)}*x^{k}'

#     return strEquation

# def printEquation(equation: str):
#     print(equation.replace('*x^1', 'x').replace('*x^0', '') + ' = 0')


# 5

# def summEquation(equation1: dict, equation2: dict):
#     finalEquation = {}

#     for i in range(max(len(equation1), len(equation2)), -1, -1):
#         if equation1.get(i) or equation2.get(i):
#             finalEquation[i] = (equation1.get(i) if equation1.get(i) else 0) + (equation2.get(i) if equation2.get(i) else 0)
#     return finalEquation
