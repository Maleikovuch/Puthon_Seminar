# 2'. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] =>[12,15,16]      ([2*6, 3*5, 4*4]);
# - [2, 3, 5, 6] => [12,15]   ( [2*6, 3*5]) 
# В скобках пример, как это работает!!!

from random import randint

list = [randint(2, 10) for i in range(5)]                  
print(list)


results = []
while len(list) > 1:
    results.append(list[0]*list[-1])
    del list[0] 
    del list[-1] 
if len(list) ==1: results.append(list[0]**2)       
print(results)

