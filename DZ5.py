# 5'. Задайте число. Составьте список чисел Фибоначчи, в том числе для отрицательных индексов.(Дополнительно)

# *Пример:*

# - для k = 8 список будет выглядеть так: [-21 ,13, -8, 5, −3, 2, −1, 1, 0, 1, 1, 2, 3, 5, 8, 13, 21] [Негафибоначчи]

n = int(input('Введите число: '))

# def fib(n):
#     if n in [1,2]:
#         return 1
#     else:
#         return fib(n-2)+fib(n-1)                # фибоначчи
# list=[]
# for i in range(1,n+1):
#     list.append(fib(i))
# print(list)

# fib = lambda n: fib(n - 1) + fib(n - 2) if n > 2 else 1   # в одну строку поиск числа
# print(fib(n))



fib = []
a, b = 1, 1
for i in range(n):
    fib.append(a)                                  # негафибоначчи
    a, b = b, a + b

a, b = 0, 1
for i in range (n+1):
    fib.insert(0, a)
    a, b = b, a - b
print(fib)

