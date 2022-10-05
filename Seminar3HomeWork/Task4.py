# <Задание 4>
# Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# Пример:
# 45 => 101101
# 3 => 11
# 2 => 10

def EnterIntNumber(question):
    number = 0
    while True:
        try:
            number = int(input(question))
            break
        except:
            print("Введеное значение не допустимо, попробуйте еще раз")
    return number


def StringRevers(str):
    ReversStr = ""
    for i in range(len(str)-1, -1, -1):
        ReversStr += str[i]
    return ReversStr


numberD = EnterIntNumber(
    "Введите десятичное целое положительное число для перевода в двоичное : ")

buffer = numberD
resultString = ""

while buffer != 0:
    resultString += str(buffer % 2)
    buffer = int(buffer/2)
print(resultString)
ReversStr = StringRevers(resultString)

print(
    f'Десятичное число {numberD} по модулю в двоичной системе исчисления = {ReversStr}')
