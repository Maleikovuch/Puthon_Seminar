# 1'. Вычислить число Пи c заданной точностью d

# *Пример:*

# - при d = 0.001, π = 3.141
# - при d = 0.0001, π = 3.1415

from math import pi

d = int(input('Введите точность (сколько знаков после запятой): \n'))
n = str(pi)
print(n[:n.find('.') + (d+1)])   # без округления


res = '{:.' + str(d) + 'f}'
print(res.format(pi))

print(round(pi, d))

print(f'{pi:.{d}f}')

