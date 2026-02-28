# Independent Event
import random

def flip_a_coin():
    choice = random.choice(['Heads', 'Tails'])
    return choice

def roll_a_dice():
    return random.randint(1, 6)

coin_result = flip_a_coin()
dice_result = roll_a_dice()
print("Coin :", coin_result)
print("Dice :", dice_result)