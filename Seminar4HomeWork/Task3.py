# Задайте последовательность цифр. Напишите программу, которая выведет список неповторяющихся элементов
# исходной последовательности.
# Пример:
# 47756688399943 -> [5]
# 1113384455229 -> [8,9]
# 1115566773322 -> []

inputString = input("Введите строку чисел : ")

result = []
rule = []

for i in range(0, len(inputString)):
    count = 0
    if inputString[i] in rule:
        continue
    for j in range(i+1, len(inputString)):
        if inputString[i] == inputString[j]:
            count += 1
            if count >= 1:
                rule.append(inputString[i])
                break
    if count == 0:
        try:
            result.append(int(inputString[i]))
        except:
            result.append(inputString[i])
print(f'Cписок уникальных элементов = {result}')
