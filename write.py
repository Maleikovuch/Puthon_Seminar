from read import read

def writed(data, name):
    with open(name, 'a+') as file:
        file.write(";".join(map(str, data)))
        file.write(f"\n")

def writing(data, name):
    with open(name, 'w') as file:
        file.write(";".join(map(str, data)))
        file.write(f"\n")
        

