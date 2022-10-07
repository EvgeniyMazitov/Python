# Создайте в файле, а потом считайте из файла строку из набора чисел.
# Напишите программу, которая покажет большее и меньшее число.
# В качестве символа-разделителя используйте пробел.

import random

size = random.randint(5, 10)
string = ''
path = r'text.txt'
pathWrite = r'newtext.txt'

for _ in range(size):
    string += f'{random.randint(1,9999)} '

with open(path, 'w', encoding='UTF-8') as data:
    data.write(string[:-1])

with open(path, 'r', encoding='UTF-8') as data:
    data_file = data.readline()


file = data_file.split(' ')

for i in range(len(file)):
    file[i] = int(file[i])
print(file)
result = str(min(file)) + ' => ' + str(max(file))

with open(pathWrite, 'w', encoding='UTF-8') as data:
    data.write(data_file + '\n')
    data.write(result)
