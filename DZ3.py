# 3'. Задайте список из вещественных чисел. Напишите программу, которая найдёт разницу между максимальным и минимальным значением дробной части элементов.

# *Пример:*
# - [1.1, 1.2, 3.1, 5, 10.01] => 0.19

# lst = list(map(float, input("Введите числа через пробел:").split()))
# print(lst)

import random
list = [round(random.uniform(1.10, 10.05),2) for i in range(5)] 
print(list)

new_list=[]
res=0
for i in list:
    i = round(i - int(i),2)
    new_list.append(i)
print(new_list)                                 # для проверки распечатаем
res = round(max(new_list)-min(new_list),2)
print(res)

# print(round(max(new_list)-min(new_list),2))


