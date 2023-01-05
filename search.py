from read import *
from output import *


def search(word, data):
    if len(data) > 0:
        for i in data:
            if word in i:
                print("---Найдены данные --- ") 
                print("id".center(5), "Фамилия".center(20), "Имя".center(10), "Класс".center(6), "Город".center(15)) 
                print("-"*120) 
                print(i[0].center(5), i[1].center(20), i[2].center(10), i[3].center(6), i[4].center(15))
                # break
        else:
               print("---Это все, что удалось найти!---")
                    
            
   
