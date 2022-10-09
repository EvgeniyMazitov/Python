# Даны два файла, в каждом из которых находится запись многочлена.
# Задача - сформировать файл, содержащий сумму многочленов.

# Пример двух заданных многочленов:
# 23x⁹ - 16x⁸ + 3x⁷ + 15x⁴ - 2x³ + x² + 20 = 0
# 17x⁹ + 15x⁸ - 8x⁷ + 15x⁶ - 10x⁴ + 7x³ - 13x¹ + 33 = 0

# Результат:
# 40x⁹ - x⁸ -5x⁷ + 15x⁶ +5x⁴ + 5x³ + x² - 13x¹ + 53 = 0

# from multiprocessing.sharedctypes import Value


path1 = 'Seminar4Homework/Mnogochlen.txt'
path2 = 'Seminar4Homework/Mnogochlen1.txt'
pathWrite = 'Seminar4Homework/MnogochlenSum.txt'


def DictinaryMaker(path):

    with open(path, 'r', encoding='UTF-8') as data:
        file = data.readline()

    data_file = file.replace(' = 0', '').replace(
        ' + ', ' ').replace(' - ', ' -').replace('*x^', ' ').replace('*x ', ' 1 ').split()

    if len(data_file) % 2 == 1:
        data_file.append('0')

    dict = {int(data_file[i+1]): int(data_file[i])
            for i in range(0, len(data_file), 2)}
    print(f'Парсинг строки файла {path}: ')
    print(data_file)
    print(f'Сформированный словарь файла {path}: ')
    print(dict)

    return dict


def UnionDict(dict1, dict2):
    dict3 = dict1.copy()
    dict3.update(dict2)

    for i in dict3:
        try:
            dict3[i] = dict1[i]+dict2[i]
        except:
            continue

    print(f'Сформированный общий словарь файла: ')
    print(f'dict3 ={dict3}')
    return dict3


def WriteStringMaker(dict):

    sorted_dict = sorted(dict.items(), reverse=True)
    writeString = ''
    for i in range(0, len(sorted_dict)):
        if sorted_dict[i][1] != 0 and writeString == '':
            writeString += str(sorted_dict[i][1])+"*x^"+str(sorted_dict[i][0])
        elif sorted_dict[i][1] != 0 and writeString == '':
            writeString += " - " + \
                str(abs(sorted_dict[i][1]))+"*x^"+str(sorted_dict[i][0])
        elif sorted_dict[i][1] > 0 and sorted_dict[i][0] not in [0, 1]:
            writeString += " + " + \
                str(sorted_dict[i][1])+"*x^"+str(sorted_dict[i][0])
        elif sorted_dict[i][1] < 0 and sorted_dict[i][0] not in [0, 1]:
            writeString += " - " + \
                str(abs(sorted_dict[i][1]))+"*x^"+str(sorted_dict[i][0])
        elif sorted_dict[i][1] > 0 and sorted_dict[i][0] == 1:
            writeString += " + " + \
                str(sorted_dict[i][1])+"*x"
        elif sorted_dict[i][1] < 0 and sorted_dict[i][0] == 1:
            writeString += " - " + \
                str(abs(sorted_dict[i][1]))+"*x"
        elif sorted_dict[i][1] > 0 and sorted_dict[i][0] == 0:
            writeString += " + " + \
                str(sorted_dict[i][1])
        elif sorted_dict[i][1] < 0 and sorted_dict[i][0] == 0:
            writeString += " - " + \
                str(abs(sorted_dict[i][1]))
    writeString += " = 0"
    print('Итоговая строка для записи в файл:')
    print(writeString)
    return writeString


dict1 = DictinaryMaker(path1)
dict2 = DictinaryMaker(path2)


dict3 = UnionDict(dict1, dict2)

writeString = WriteStringMaker(dict3)

with open(pathWrite, 'w', encoding='UTF-8') as data:
    data.write(writeString)
