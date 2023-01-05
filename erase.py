from enter_data import data
from write import writing

                    
def erase(data):
    index = int(input('Введите индекс пользователя, которого необходимо удалить: '))
    
    del data[index]
    writing(data, "student.csv")
    print("Данный контакт удален")
    
    


