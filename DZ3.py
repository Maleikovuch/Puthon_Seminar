# Задайте список из n чисел последовательности (1+1/n)^n и выведите на экран их сумму.

# Пример:

# - Для n = 6: [2.0, 2.25, 2.37037037037037, 2.44140625, 2.4883199999999994, 2.5216263717421135]
from decimal import Decimal
from fractions import Fraction
n = int(input('Введите количество чисел в списке '))

list = []
for i in range(1, n+1):
    i = (1+1/i)**i
    list.append(i)
print(list)
# sum=0
# for i in list:
#     sum = sum +i
# print (f'Сумма чисел из списка ->', sum_elements)

sum_numbers = sum(list)
print(f'Сумма чисел из списка ->', sum_numbers)
