# 4'. Напишите программу, которая будет преобразовывать десятичное число в двоичное.

# *Пример:*

# - 45 -> 101101
# - 3 -> 11
# - 2 -> 10

# первый вариант
n = int(input())
res=''
while n > 0:
    res = str(n % 2) + res
    n //= 2
print(res)

# второй вариант

#print(bin(n))
print(format(n, 'b'))

