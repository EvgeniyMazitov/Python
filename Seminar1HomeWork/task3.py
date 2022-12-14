# Напишите программу, которая принимает на вход координаты точки (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

coordX = float(input('Введите координату X'))
coordY = float(input('Введите координату Y'))

if coordX == 0 or coordY == 0:
    print('Вы ввели точку начала координат')
elif coordX > 0 and coordY > 0:
    print('Введенная точка расположена в 1-ой четверти')
elif coordX < 0 and coordY > 0:
    print('Введенная точка расположена во 2-ой четверти')
elif coordX < 0 and coordY < 0:
    print('Введенная точка расположена в 3-ей четверти')
elif coordX > 0 and coordY < 0:
    print('Введенная точка расположена в 4-ой четверти')
elif coordX == 0:
    print('Введенная точка расположена на оси Y')
elif coordY == 0:
    print('Введенная точка расположена на оси X')
