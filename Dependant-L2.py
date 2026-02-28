# Dependant Event
import random

def draw_a_candy(bag):
    candy = random.choice(bag)
    bag.remove(candy)
    return candy

bag_of_candies = ['White', 'Yellow', 'Blue', 'Pink']


# Drawing first candy

print("\nProbability for the first candy drawn is", 1/len(bag_of_candies))

first_candy = draw_a_candy(bag_of_candies)
print("Your first candy drawn is", first_candy)
print("Remaining candies in the bag :", bag_of_candies)


# Drawing second candy

print("\nProbability for the first candy drawn is", 1/len(bag_of_candies))

second_candy = draw_a_candy(bag_of_candies)
print("\nYour second candy drawn is", second_candy)
print("Remaining candies in the bag :", bag_of_candies)



"""Finding the probability for the first candy
 print("\nProbability for the first candy drawn is", 1/4)
 Finding the probability for the second candy
 print("\nProbability for the second candy drawn is", 1/3)"""