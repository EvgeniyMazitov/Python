import random

maxAll = 150
max1 = 29
fail = [0, maxAll]

for i in range(maxAll - 29, -1, -max1):
    fail.insert(-1, maxAll-i)

print(fail)
current = 150
need = 0
for i in range(0, len(fail)):
    if current == maxAll:
        need = maxAll-fail[-2]
    elif current == fail[i]:
        need = random.randint(1, min(25, current))
    elif fail[i] < current < fail[i+1]:
        need = current-fail[i]
print(need)

print(150-(150-150 % 29))
