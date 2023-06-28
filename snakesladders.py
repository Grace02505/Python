import random

ladder = {1: 38, 4: 14, 9: 31, 21: 42, 28: 84, 51: 67, 72: 91, 80: 99}
snake = {7: 17, 18: 62, 34: 54, 36:87, 60: 64, 73: 93, 75: 95, 79: 98}
pos1 = 0
pos2 = 0


def move(pos):
    dice = random.randint(1, 6)
    print(f"Dice:{dice}")
    pos = pos + dice
    if pos in snake:
        print("Bitten by snake")
        pos = snake[pos]
        print(f"Position:{pos}")
    elif pos in ladder:
        print("Climbed by ladder")
        pos = ladder[pos]
        print(f"Position:{pos}")
    else:
        print(f"Position:{pos}")
    print("\n")
    return pos

while True:
    A = input("Player 1 Enter \"A\" to throw dice:")
    pos1 = move(pos1)
    if pos1 >= 100:
        print("Game Over!\n Player 1 wins.")
        break
    B = input("Player 2 Enter \"B\" to throw dice:")
    pos2 = move(pos2)
    if pos2 >= 100:
        print("Game Over!\n Player 2 wins.")
        break




        
