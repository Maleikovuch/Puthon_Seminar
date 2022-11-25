# Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.

# Пример:

# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

from math import sqrt


print('Введите координаты первой точки A: ')
ax = float(input())
ay = float(input())
print('Введите координаты второй точки B:')
bx = float(input())
by = float(input())

r = (bx-ax)**2 + (by-ay)**2
rrr = sqrt (r)

print(f'Расстояние между точками A и B -> {rrr} ')


# r = round(((bx-ax)*(bx-ax) + (by-ay)*(by-ay))**0.5,3)
# print(f'Расстояние между точками A и B -> {r} ')


# r = ((bx-ax)*(bx-ax) + (by-ay)*(by-ay))
# rr = pow(r, 0.5)
# print(f'Расстояние между точками A и B -> {rr} ')


