# Задайте натуральное число N. Напишите программу, которая составит список простых множителей числа N.

def EnterInt(question):
    number = 0
    while True:
        try:
            number = int(input(question))
            if number < 2:
                print("Введеное значение не допустимо, попробуйте еще раз")
                continue
            break
        except:
            print("Введеное значение не допустимо, попробуйте еще раз")
    return number


numberN = EnterInt('Введите натуральное число N>=2: ')

result = []
minDel = 2
bufferN = numberN

while (minDel <= bufferN):
    if bufferN % minDel == 0:
        result.append(minDel)
        bufferN /= minDel
    else:
        minDel += 1
print(f'Список простых множителей числа {numberN}:')
print(result)
