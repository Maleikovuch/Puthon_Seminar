a = (input('Введите вещественное число: '))
# str_a = str(a)
# str_a = str_a.replace('.', '')
# lst_str = list(str_a)
# lst_num = map(int, lst_str)
# s = sum(lst_num)
# print(f'Сумма цифр числа', a, 'равна', s)


s = sum(map(int, str(a).replace('.', '')))          
print(f'Сумма цифр числа', a, 'равна', s)