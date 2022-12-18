def search(base, contact):
    base = base.split()
    flag = True
    results = []
    for i in base:
        if contact in i:
            flag = False
            results.append(i)
    if flag:
        print(f'Данные {contact} не найдены')
    return results
