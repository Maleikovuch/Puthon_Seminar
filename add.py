from enter_data import data
from write import writed



def add():
    dct = data()
    writed([dct.get("id"), dct.get("surname"), dct.get("name"), dct.get("class"), dct.get("city")], "student.csv")
    
    print("---Данные добавлены!---")

