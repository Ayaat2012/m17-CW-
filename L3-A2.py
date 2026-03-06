#Consider, there is a bowl of 6 orange and 4 blue balls. 
#Event A is selecting 1st Orange ball and 
#event B is selecting 2nd Blue ball. 
# Find the probability of both events occurring by using multiplication rule.


def prob_a_b(orange, blue, total):
    # Probability of getting 1st orange
    prob_a = orange / total

    # Probability of getting 2nd blue
    prob_b_given_a = blue / (total - 1)

    # Probability of intersection of events a and b
    prob_a_and_b = prob_a * prob_b_given_a
    return round(prob_a_and_b, 2)


orange = int(input("Enter number of orange balls "))
blue = int(input("Enter number of blue balls "))
total = orange + blue

print("Probability of getting, 1st, orange and 2nd, blue ball :", prob_a_b(orange, blue, total))