# Simulate the outcome of rolling a fair dice with n sides for given number of times.
import numpy as np

dice_sides = int(input("Enter the number of sides of the dice [6/12] "))
dice = range(1, dice_sides + 1)

num_of_rolls = int(input("Enter the number of rolls "))

result = np.random.choice(dice, size=num_of_rolls, replace=True)
print(f"Outcome is {result}")