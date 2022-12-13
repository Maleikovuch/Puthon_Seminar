from random import randint

list_data = [randint(2, 10) for i in range(20)]
print(list_data)

list_new = []
for i in list_data:
    if list_data.count(i) == 1:
        list_new.append(i)
print(list_new)



new_list = list(filter(lambda x: list_data.count(x) == 1, list_data ))   
print(list_new)