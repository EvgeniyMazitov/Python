# 2. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.

#     Примеры:

#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90


# a = int(input('Введите 1е число a:'))
# b = int(input('Введите 2е число b:'))
# c = int(input('Введите 2е число b:'))
# d = int(input('Введите 2е число b:'))
# e = int(input('Введите 2е число b:'))

# fmax = max(a, b, c, d, e)

# print(fmax)


arrayInt = []
for i in range(5):
    arrayInt.append(int(input(f'Введите {i+1} число ')))
print(arrayInt)

maxx = arrayInt[0]

for i in range(1, len(arrayInt)):
    if maxx <= arrayInt[i]:
        maxx = arrayInt[i]

# for i in arrayInt:
#     if maxx <= i:
#         maxx = i
print(f'максимальное значение в списке {arrayInt} будет {maxx}')
