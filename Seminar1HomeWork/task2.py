# Напишите программу для. проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.
arrayX = [0, 1]
arrayY = [0, 1]
arrayZ = [0, 1]
flag = True
print('}X  |Y  |Z  |f1 |f2 |')
for i in arrayX:
    for j in arrayY:
        for k in arrayZ:
            function1 = int(not (arrayX[i] or arrayY[j] or arrayZ[k]))
            function2 = int(not arrayX[i] and not arrayY[j] and not arrayZ[k])
            print(f'|{i}  |{j}  |{k}  |{function1}  |{function2}  |')
            if function1 != function2:
                flag = False
if flag == False:
    print('Доказано, что утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z неверно для любых X,Y,Z')
else:
    print('Доказано, что утверждение ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z верно для любых X,Y,Z')
