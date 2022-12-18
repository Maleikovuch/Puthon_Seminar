def new(contact):
    with open ('book.txt', 'a', encoding='utf-8') as book:
        book.write(f'\n{contact}')
        
def old(contact):
    with open ('book.txt', 'r', encoding='utf-8') as book:
        return book.read()