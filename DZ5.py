# Реализуйте алгоритм перемешивания списка.
import random
from random import randint

# list=[1,2,3,4,5,6]
# print(list)
# random.shuffle(list)
# print(list)


my_list = list(range(1, 20))
print(f'Начальный список    ', my_list)
random.shuffle(my_list)
print(f'Перемешанный список ', my_list)


# list=[]
# for i in range(15):
#     list.append(randint(-10,10))
# print(list)
# random.shuffle(list)
# print(list)
