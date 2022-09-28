# типы данных и переменная
# int, float, boolean, str, list, None
# value = None
# print(type(value))
# a = 123
# b = 1.23
# print(type(a))
# print(type(b))
# value = 12334
# print(type(value))
# s = 'hello world'
#s1 = 'hello "world'
# l = "hello 'world"
# m = 'hello \'world'
# k = 'hello \nworld'
# print(s)  # Вывод строки
# print(l)  # Вывод строки
# print(m)  # Вывод строки
# print(k)  # Вывод строки
# print(s, l, m)
# print(a, '-', b, '-', s)
# print('{} - {} - {}'.format(a, b, s))
# print(f'{a} - {b} - {s}')
# print('{1} - {2} - {0}'.format(a, b, s))

# f = True
# print(f)
# list = []
# print(list)
# list1 = ['1', '2', '3', 'hello']
# print(list1)
# list2 = [1, 2, 3, 4]
# print(list2)
# list3 = ['1', '2', '3', 'hello', 1, 2, 3, 4, True]
# print(list3)

# print('Введите a')
# a = int(input())
# print('Введите b')
# b = float(input())
# print(a, ' ', b, ' ', a+b)
# print('{} {}'.format(a, b))
# print(f'{a} {b}')

# a = 1.31231231
# b = 3
# c = round(a * b, 7)
# print(c)

# a = 1 < 4 and 5 > 2
# a = 'qwe'
# b = 'qwe'
# print(a == b)
# a = [1, 2]
# b = [1, 2]
# print(a == b)

# a = 1 < 3 < 5 < 10
# print(a)

# func = 1
# T = 4
# x = 2
# print(func < T > x)

# f = 1 > 2 or 4 < 6
# f = [1, 2, 3, 4]
# print(f)
# print(not 2 in f)

# is_odd = f[0] % 2 == 0
# is_odd = not f[0] % 2
# print(is_odd)

# a = int(input('a = '))
# b = int(input('b = '))
# if a > b:
#     print(a)
# else:
#     print(b)

# username = input('Введите имя ')
# if username == 'Маша':
#     print('Ура, это же МАША!')
# elif username == 'Марина':
#     print('Я так ждала вас, Марина!')
# elif username == 'Женя':
#     print('Женя - топ')
# else:
#     print('Привет, ', username)

# original = 2312
# inverted = 0
# while original != 0:
#     inverted = inverted*10+(original % 10)
#     original //= 10
#     print(original)
# else:
#     print('Пожалуй')
#     print('Хватит )')
# print(inverted)

# list = [1, 2, 7, 4, 5]
# for i in list:
#     print(i**2)

# for i in 1, 2, 3, 4, 5:
#     print(i**2)

# r = range(10)
# for i in r:
#     print(i)

# for i in range(1, 10, 2):
#     print(i)

# for i in 'qwe - rty':
#     print(i)

# text = 'съешь еще этих мягких французских булок'
# print(len(text))
# print('еще' in text)
# print(text.isdigit())
# print(text.islower())
# print(text.replace('еще', 'ЕЩЕ'))

# for c in text:
#     print(c)

# help(text.istitle)

# print(text[0])
# print(text[1])
# print(text[len(text)])
# print(text[len(text)-1])
# print(text[:])
# print(text[:2])
# print(text[len(text)-2:])
# print(text[2:9])
# print(text[6:-18])
# print(text[0:len(text):6])
# print(text[::6])
# text = text[2:9]+text[-5]+text[:2]

# numbers = [1, 2, 3, 4, 5]
# print(numbers)
# ran = range(1, 6)
# print(type(ran))
# numbers = list(ran)
# print(type(numbers))

# print(numbers)
# numbers[0] = 10
# print(f'{len(numbers)} len')
# print(numbers)
# for i in numbers:
#     i *= 2
#     print(i)
# print(numbers)


# colors = ['red', 'green', 'blue']

# for e in colors:
#     print(e)

# for e in colors:
#     print(e*2)

# colors.append('gray')
# print(colors == ['red', 'green', 'blue', 'gray'])
# colors.remove('red')  # del colors[0] # удалить элемент
# print(colors)


def f(x):
    if x == 1:
        return 'Целое'
    elif x == 2.3:
        return 23
    else:
        return


arg = 1
print(f(arg))
print(type(f(arg)))
