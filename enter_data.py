from read import count


def data():
    dct = dict()
    Id = count("student.csv")
    dct["id"] = Id     
    dct["surname"] = input('Введите Фамилию: ')
    dct["name"] = input('Введите Имя: ')
    dct["class"] = input('Введите Класс: ') 
    dct["city"] = input('Введите Город: ')   
    return dct
