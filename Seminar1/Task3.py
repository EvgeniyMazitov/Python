# 1. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N

#     *Примеры:*

#     - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5

N = int(input('N равно: '))
array = []
# for i in range(-N, N+1):
#     array.append(i)
# print(array)

# for i in range(-N, N+1):
#     print(i, end=', ')

for i in range(-N, N):
    print(i, end=', ')
print(N)


for i in range(-N, N+1):
    if i != N:
        print(i, end=', ')
    else:
        print(N)
