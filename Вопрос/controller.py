import view
import model
from random import randint
import logger


def run():
    while view.candies > 28:
        if view.choice:
            k = model.step_player(view.player1)
            view.candies -= k
            view.choice = False
            print(f"Вы взяли {k} конфет, осталось {view.candies} конфет.")
        else:
            k = model.step_bot(view.candies)
            view.candies -= k
            view.choice = True
            print(f"БОТ взял {k}, осталось {view.candies} конфет.")


run()


def win():
    if view.choice:
        print(f"Выиграл {view.player1}")
    else:
        print(f"Выиграл {view.player2}")


win()
result = f'{win}'
# print(result)

