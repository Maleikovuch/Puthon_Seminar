from random import randint
import view


def step_player(name):
    x = int(input(f"{name}, возьмите конфет не более  28 штук: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x
    

def step_bot(k):
    return randint(1, 29)
    