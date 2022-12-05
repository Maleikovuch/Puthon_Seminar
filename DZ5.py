# 5. Даны два файла, в каждом из которых находится запись многочлена. Задача - сформировать файл, содержащий сумму многочленов.

# В file1.txt :
# 2*x**2 + 4*x + 5

# В file2.txt:
# 4*x**2 + 1*x + 4

# Результирующий файл:
# 6*x**2 + 5*x + 9

import sympy

with open('file1.txt', 'r') as data:
    poly1 = data.readline()
with open('file2.txt', 'r') as data:
    poly2 = data.readline()

poly_sum = str(sympy.simplify(f'{poly1} + {poly2}'))

with open('file_res.txt', 'w') as data:
    data.write(poly_sum)

# print(poly_sum)
