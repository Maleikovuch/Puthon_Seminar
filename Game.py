from random import randint

player1 = input("Введите имя первого игрока: ")
player2 = "Bot"
candies = int(input("Введите количество конфет на столе: "))

players = randint(0, 1)
if players:
    print(f"Первый ходит {player1}")
else:
    print(f"Первый ходит {player2}")
    
def step_player(name):
    x = int(input(f"{name}, возьмите конфет не более  28 штук: "))
    while x < 1 or x > 28:
        x = int(input(f"{name}, введите корректное количество конфет: "))
    return x

def step_bot(candies):
    y = randint(1, 29)
    return y

while candies > 28:
    if players:
        k = step_player(player1)
        candies -= k
        players = False
        print(f"Вы взяли {k} конфет, осталось {candies} конфет.")
    else:
        k = step_bot(candies)
        candies -= k
        players = True
        print(f"БОТ взял {k}, осталось {candies} конфет.")

if players:
    print(f"Выиграл {player1}")
else:
    print(f"Выиграл {player2}")


