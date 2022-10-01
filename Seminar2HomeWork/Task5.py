# НЕОБЯЗАТЕЛЬНО Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях. Позиции хранятся в файле file.txt в одной строке одно число.

def EnterIntNumber(question):
    number = 0
    while True:
        try:
            number = int(input(question))
            break
        except:
            print("Введеное значение не допустимо, попробуйте еще раз")
    return number


numberN = EnterIntNumber("Введите число элементов для списка N: ")

list = []
for i in range(-numberN, numberN+1):
    list.append(i)
print(list)

path = 'Seminar2HomeWork/text.txt'
data = open(path, 'r')
result = 1
print('Данные из файла:')
for line in data:
    try:
        result *= list[int(line)]
        print(line, end="")
    except:
        print(
            f'Одно из значений файла не входит в диапазон индексов списка ({line}) и не будет учтено в итоговом произведении')

data.close()
print()
print(f'Произведение значений списка на позициях из файла = {result}')
