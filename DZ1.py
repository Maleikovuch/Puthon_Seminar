# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

# a = float(input())
# sum = 0
# while (a != 0):
#     sum = sum+a % 10
#     a = a // 10
# print(sum)

a = float(input())
str_a = str(a)
str_a = str_a.replace('.', '')
lst_str = list(str_a)
lst_num = map(int, lst_str)
s = sum(lst_num)
print(s)




