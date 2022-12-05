# 3'. Задайте последовательность чисел. Напишите программу, которая выведет список неповторяющихся элементов исходной последовательности.

from random import randint

list = [randint(2, 10) for i in range(20)]
print(list)

list_new = []
for i in list:
    if list.count(i) == 1:
        list_new.append(i)
print(list_new)



           
            
