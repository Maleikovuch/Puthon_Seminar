# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

print('Введите значение для X: ')
X = int(input())
print('Введите значение для Y: ')
Y = int(input())
print('Введите значение для Z: ')
Z = int(input())

if not (X or Y or Z) == (not X and not Y and not Z):
    print('Верно')
else:
    print('Не верно')
