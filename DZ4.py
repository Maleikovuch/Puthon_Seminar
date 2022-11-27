# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.
# (для продвинутых - с файлом, вариант минимум - ввести позиции в консоли) -2 -1 0 1 2 Позиции: 0,1 -> 2


n = int(input('Введите число: '))

# list = []
# for i in range(-n, n+1):
#     list.append(i)
# print(list)


my_list = list(range(-n, n+1))
print(f'Заданный список -', my_list)

# pos = file.read().splitlines()                      # переход на новую строку не используем (readlines нельзя),
# print(list(map(int, s)))                            # print(s)  result = list(map(int, s))    print(result); выведет в виде [0, 1],
                                                     
                                                    #поменяется только отображение вывода, сам тип не изменится

# for i in pos:                                       # выведет в виде     0
#     print(i)                                        #                    1,  то есть выведет каждый элемент по отдельности

with open("position.txt", "r") as file:
   pos = list(map(int, file.readlines()))            #здесь уже поменяли именно тип и вывели его уже измененный
print(f'Позиции из файла - ', pos)                                              

mult = 1
for i in range(len(pos)):
    mult *= my_list[pos[i]]
print(f'Произведение элементов на указанных позициях ->', mult)

