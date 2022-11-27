# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр.

# Пример:

# - 6782 -> 23
# - 0,56 -> 11

# a = float(input())
# sum = 0
# while (a > 0):                                #Для вещественных чисел не подходит
#     sum = sum+a % 10
#     a = a // 10
# print(sum)

a = (input('Введите вещественное число: '))
# str_a = str(a)
# str_a = str_a.replace('.', '')
# lst_str = list(str_a)
# lst_num = map(int, lst_str)
# s = sum(lst_num)
# print(f'Сумма цифр числа', a, 'равна', s)


s = sum(map(int, str(a).replace('.', '')))          #Сокращенный вариант
print(f'Сумма цифр числа', a, 'равна', s)
