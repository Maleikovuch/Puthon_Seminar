def contact_find():
    return input("Что ищем: ")

def choice():
    return input("1-добавить, 2-найти \n")

def contact_new():
    name=input("Имя- ")
    phone=input("Номер телефона- ")
    return f'{name} / {phone}'

def find(result):
    print("Что нашли: ")
    for i in result:
        print(i)