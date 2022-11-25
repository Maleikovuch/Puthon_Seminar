# Задайте список из N элементов, заполненных числами из промежутка [-N, N]. Найдите произведение элементов на указанных позициях.
# Позиции хранятся в файле file.txt в одной строке одно число.
# (для продвинутых - с файлом, вариант минимум - ввести позиции в консоли) -2 -1 0 1 2 Позиции: 0,1 -> 2


n = int(input('Введите количество элементов '))

# list = []
# for i in range(-n, n):
#     list.append(i)
# print(list)


h=list(range(-n,n))
print(h)

with open("file.txt", "r") as file:
    s=file.read().splitlines()                   #переход на новую строку не используем (readlines нельзя), #print(s)
    print(list(map(int, s)))                     #print(s)  result = list(map(int, s))    print(result)
 
     
 


