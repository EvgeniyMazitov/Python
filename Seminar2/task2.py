# 2. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.

#     *Пример:*

#     - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

# dict = {}

# dict = {3: 'Привет', 8: 'Пока'}

# print(dict[3])

# print(dict.get(8))
# print(dict.get(8))

n = int(input('Введите число N: '))
dict = {}
for i in range(1, n+1):
    dict[i] = 3*i+1

print(dict)
dict[4] = "Мы изменили тебя"
print(dict.get(8))
print(dict)
