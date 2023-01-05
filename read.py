def read():
    lst_name = []
    with open('student.csv', 'r') as file:
        for line in file:
            temp = line.strip().split(';')
            lst_name.append(temp)
           
    lst = []
    for i  in range(len(lst_name)):
        lst.append([lst_name[i][0], lst_name[i][1], lst_name[i][2], lst_name[i][3], lst_name[i][4]])
    return lst

def count(student):
    with open(student, 'r') as file:
        data = file.read()
    return data.count('\n')