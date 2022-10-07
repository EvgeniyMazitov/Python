# from random import randint as rI

# number = int(input('Введите размер списка: '))

# myList = []

# for i in range(number):
#     myList.append(rI(-10,10))

# print(myList)

# listLenght = len(myList)

# multiList = []
# for i in range(listLenght//2+1):
#     element = myList[i]*myList[listLenght-i-1]
#     multiList.append(element)


# print(multiList)


# from random import uniform as uI
# from random import randint as rI
# from decimal import Decimal

# number = int(input('Введите размер списка: '))

# myList = []

# for i in range(number):
#     coef = rI(1,4)
#     number = Decimal(f'{round(uI(-10,10), coef)}')
#     myList.append(number)


# numList = []
# mantissa = []

# for num in myList:
#     numList.append(float(num))
#     if abs(num) - int(abs(num)) != 0.0:
#         mantissa.append(abs(num) - abs(int(num)))

# print(numList)
# print(f'Максимальная {max(mantissa)} и минимальная {min(mantissa)} мантиссы')
# print(f'Разница мантисс {max(mantissa) - min(mantissa)}')


# number = int(input('Введите число в десятичной системе: '))

# num = number
# binaryNumber = []

# while number>0:
#     binaryNumber.insert(0, str(number%2))
#     number //= 2

# print(binaryNumber)
# print(f"Число {num} в двоичной системе {''.join(binaryNumber)}")
