#Suppose that the following is true (this is shown in the first set of branches in the diagram): 
# - 20 percent of the population has strep throat. 
# - 80 percent of the population does not have strep throat. 
#Now suppose that we test a bunch of people for strep throat. 
#The possible results of these tests are shown in the next set of branches: 
# - If a person has strep throat, there is an 85% chance their test will be positive and a 15% chance it will be negative.
# - If a person does not have strep throat, there is a 98% chance their test will be negative and a 2% chance it will be positive


print("Let's calculate probability. Please enter choices for events...")

print("Person has strep throat?\n1. Yes\n2. No")
a = int(input("Enter your choice (1/2) "))

print("Person has tested positive?\n1. Yes\n2. No")
b = int(input("Enter your choice (1/2) "))


def find_prob(a,b):
    if a == 1:
        prob_a = 0.2
        if b == 1:
            prob_b_given_a = 0.85
        elif b == 2:
            prob_b_given_a = 0.15
        else:
            print("Invalid input")

    elif a == 2:
        prob_a = 0.8
        if b == 1:
            prob_b_given_a = 0.02
        elif b == 2:
            prob_b_given_a = 0.98
        else:
            print("Invalid input")

    else:
        print("Invalid input")

    prob_a_and_b = prob_a * prob_b_given_a
    print("Probability of both events happening :", round(prob_a_and_b, 2))


print("Probabilities for event a and b :")
find_prob(a,b)