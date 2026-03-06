#There are 2 red shirts, 4 blue shirts, and 9 white shirts in a basket. 
#Two shirts are randomly selected. 
# Find the probability that the second shirt is red given that the first shirt is blue. 
#(Assume that the first shirt is replaced). 


red_shirt = int(input("Enter number of red shirts "))
blue_shirt = int(input("Enter number of blue shirts "))
white_shirt = int(input("Enter number of white shirts "))

total = red_shirt + blue_shirt + white_shirt

prob_a = blue_shirt / total
prob_b = red_shirt / total

prob_b_given_a = prob_b
prob_a_and_b = prob_a * prob_b

print("Probability that the second shirt is red given that the first shirt is blue :")
print(round(prob_b_given_a, 3))
print("Probability that the second shirt is red and the first shirt is blue :")
print(round(prob_a_and_b, 3))