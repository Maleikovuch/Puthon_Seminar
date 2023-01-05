from add import *
from read import *
from output import *
from search import *
from erase import *

def greet():
    print("---Здравствуйте!---")

def start():
    print("_"*100)
    print("Что нужно сделать:\n\
    1 - получить информацию об учениках;\n\
    2 - добавить ученика в список;\n\
    3 - найти ученика;\n\
    4 - удалить ученика из списка;\n\
    5 - выйти.")
    n = input("Введите цифру: ")
    
    if n == '1':
        data = read()
        output(data)
        start()
    elif n == '2':
        add()
        start()
    elif n == '3':
        info = input("Для поиска введите одно из значений(id, Фамилия, Имя, Класс, Город): ")
        data = read()
        item = search(info, data)
        start()
    elif n == '4':  
        info = input("Для поиска введите одно из значений(id, Фамилия, Имя, Класс, Город): ")
        data = read()
        item = search(info, data)
        erase(data)
        start() 
    elif n == '5':
        print("До свидания!")
    else:
        print("---Введите корректное значение---")
        start()
