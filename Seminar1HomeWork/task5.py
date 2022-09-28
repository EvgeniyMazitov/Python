# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

def InputCoord():
    arrayCoord = []
    for i in range(2):
        arrayCoord.append(int(input(f'Введите {i+1}-ю координату точки: ')))
    return arrayCoord


print('Ввод координат точки A')
arrayCoordA = InputCoord()
print('Ввод координат точки B')
arrayCoordB = InputCoord()

lang = round(pow((((arrayCoordB[0]-arrayCoordA[0])**2) +
                  ((arrayCoordB[1]-arrayCoordA[1])**2)), 0.5), 2)

print(
    f'длина отрезка A({arrayCoordA[0]};{arrayCoordA[1]}) B({arrayCoordB[0]};{arrayCoordB[1]}) равна {lang}')
