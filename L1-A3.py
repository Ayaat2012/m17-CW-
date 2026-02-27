#Write a function to find the probability of picking up a red ball 
#from a bowl of blue, red, and green colored balls. 
#Then, pick a ball of any color using a random function and 
#then check whether Red Ball was picked or not.

import random

def pick_a_ball(red, blue, green):
    bowl = ['red'] * red + ['blue'] * blue + ['green'] * green
    print("Bowl", bowl)
    picked = random.choice(bowl)

    if picked == "red":
        print("You have gotten the red ball!")
    else:
        print("No red ball. Try again")

def find_prob(red, blue, green):
    total = red + blue + green
    return red / total

# Values
red = 5
blue = 3
green = 2

# Calling the finctions
print("Probability is ", find_prob(red, blue, green))
pick_a_ball(red, blue, green)