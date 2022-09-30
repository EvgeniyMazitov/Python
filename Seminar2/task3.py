# Напишите программу, в которой пользователь будет задавать две строки, а программа - определять количество вхождений одной строки в другой.

# string = "hsgfcwenfasfdasdfsagfgjfwenjkwwqfdgwenvdsf"
# substring = "wen"
# count = 0
# for i in range(len(string)-4):
#     if string[i] == substring[0] and string[i+1] == substring[1] and string[i+2] == substring[2]:
#         count += 1
# print(count)


string = "hsgfcwenwentfasfdasdfsagfgjfwenjkwwqfdgwenvdsfwent"
substring = "went"
count = 0
buffer = 0
lengthSubstring = len(substring)
lengthString = len(string)
for i in range(lengthString - lengthSubstring+1):
    for j in range(lengthSubstring):
        if string[i+j] != substring[j]:
            buffer = 0
            break
        elif string[i+j] == substring[j]:
            buffer += 1
            if buffer == lengthSubstring:
                count += 1
                buffer = 0
            continue
print(count)


# string = input('Введите строку: ')
# substring = input('Введите строку для поиска: ')
# n = 0

# if string.find(substring) == -1:
#     print("Совпадений нет")
# else:
#     n = 1
#     new_string = string[(string.find(substring) + len(substring)):]
#     while new_string.find(substring) != -1:
#         n += 1
#         new_string = new_string[(new_string.find(substring) + len(substring)):]

# print(n)


# string = "afgakwenwenhja;uicaweniuwgweneawen"
# subString = "wen"

# print(string.count(subString))

# total = 0

# for i in range(len(string)-len(subString)+1):
#     count = 0
#     if string[i] == subString[0]:
#         for j in range(len(subString)):
#             if string[i+j] == subString[j]:
#                 count += 1
#         if count == len(subString):
#             total += 1

# print(f"Строка '{subString}' входит в строку '{string}' - {total} раз")

# counter = 0

# for i in range(len(string)):
#     if string[i:i+len(subString)] == subString:
#         counter += 1

# print(f'Количество вхождений - {counter}')
