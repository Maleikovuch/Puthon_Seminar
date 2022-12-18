import controller

def base(result):        
    with open('file_res.txt', 'w') as data:
        data.write(f'{result}')
            