# 4'. Задана натуральная степень k. Сформировать случайным образом список коэффициентов (значения от 0 до 100) многочлена и записать в файл многочлен степени k.

# Пример:

# k=2 => 2*x*2 + 4*x + 5 = 0 или x2 + 5 = 0 или 10*x*2 = 0
# k=3 => 2*x*3 + 4*x*2 + 4*x + 5 = 0 5'
import random


k= int(input('Задайте степень (введите натуральное число): '))
polynomial = ""
for i in range(k+1):
    coef = random.randint(0, 100)
    if coef != 0 and i < k-1:
        polynomial = polynomial + f"{coef}*x**{k-i} + "
    elif coef != 0 and i == (k-1):
        polynomial = polynomial + f"{coef}*x + "
    elif coef != 0:
        polynomial = polynomial + f"{coef}"
        
with open('file_poly.txt', 'w') as data:
    data.write(polynomial)
# print(polynomial)