# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x¹ + 33 = 0

# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x¹ + 53 = 0

path1 = 'Seminar4Homework/Mnogochlen.txt'
path2 = 'Seminar4Homework/Mnogochlen1.txt'


with open(path1, 'r', encoding='UTF-8') as data:
    file = data.readline()

koeff_file = file.replace(' = 0', '').replace(
    ' + ', ' ').replace(' - ', ' -').replace('*x^2', '').replace('*x', '').split()
stepen_file = file.replace(' = 0', '').replace(
    ' + ', ' ').replace(' - ', ' -').replace('*x**2', '').replace('*x', '').split()

print(koeff_file)
print(stepen_file)
