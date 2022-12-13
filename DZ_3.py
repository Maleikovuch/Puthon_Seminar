# 1'. Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# *Пример:*

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint

list = [randint(2, 10) for i in range(5)]
sum = 0
for i in range(len(list)):
    if i % 2 != 0:
        sum += list[i]
print(f"Сумма равна:", sum)


list = [randint(2, 10) for i in range(5)]
sum = 0
for i, y in enumerate(list):
    if i % 2 != 0:
        sum += y
    print(f"Сумма равна:", sum)