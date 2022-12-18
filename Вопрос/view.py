from random import randint


player1 = input("Введите имя первого игрока: ")
player2 = "Bot"
candies = int(input("Введите количество конфет на столе: "))
 

def choice():
    players = randint(0, 1)
    if players:
        print(f"Первый ходит {player1}")
    else:
        print(f"Первый ходит {player2}")
choice ()