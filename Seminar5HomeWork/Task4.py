# 4. Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных. Входные и выходные данные хранятся в отдельных текстовых файлах.

# Пример: aaaaaaabbbbbbcccccccccd => 7a6b9c1d или 11a3b7c1d => aaaaaaaaaaabbbcccccccd

pathInputString = 'Seminar5Homework/InputString.txt'
pathWrightZip = 'Seminar5Homework/Zipped.txt'
pathWrightUnZip = 'Seminar5Homework/UnZipped.txt'


def StrZip(inputStr: str):
    zipStr = ''
    testChar = ''
    count = 1
    for i in inputStr:
        if i != testChar:
            if testChar:
                zipStr += str(count)+testChar
            count = 1
            testChar = i
        else:
            count += 1
    else:
        zipStr += str(count)+testChar
    return zipStr


def StrUnZip(zipStr: str):
    unzipStr = ''
    for i in range(0, len(zipStr), 2):
        unzipStr += zipStr[i+1]*int(zipStr[i])
    return unzipStr


with open(pathInputString, 'r', encoding='UTF-8') as data:
    inputStr = data.readline()

print(f'Считанная строка из файла {pathInputString}: {inputStr}')

zipStr = StrZip(inputStr)
print(f'Закодированная строка из файла {pathWrightZip}: {zipStr}')

with open(pathWrightZip, 'w', encoding='UTF-8') as data:
    data.write(zipStr)

unzipStr = StrUnZip(zipStr)

with open(pathWrightUnZip, 'w', encoding='UTF-8') as data:
    data.write(unzipStr)

print(f'Раскодированная строка из файла {pathWrightUnZip}: {unzipStr}')
