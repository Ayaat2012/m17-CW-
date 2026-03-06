#Back at the College of Knowledge, 30% of the students are Freshmen. 
#If a student is a Freshman, there is a 75% chance she eats in the dining hall. 
#If a student is not a Freshman, there is a 60% chance she eats in the dining hall. 
#We are interested in some probabilities when we pick a student at random. 
# (a) The probability of a student who eats in the dining hall if the student is a Freshman 
# (b) The probability of getting a Freshman who eats in the dining hall


def find_prob(a,b):
    if a == 1:
       prob_a = 0.30
       if b == 1:
           prob_b = 0.75
       else:
           prob_b = 0.25
    
    else:
        prob_a = 0.70
        if b == 1:
            prob_b = 0.60
        else:
            prob_b = 0.40

    prob_a_and_b = prob_a * prob_b
    return round(prob_a_and_b, 2)


print("Check the probability of any event occurring. First enter your choices.")

print("Is the student a Freshman? \n1. Yes \n2. No")
a = int(input("Enter your choice (1/2)"))

print("Is the student eating in the dining hall? \n1. Yes\n2. No")
b = int(input("Enter  your choice (1/2)"))

print("Here is the probability of both the events occurring :", find_prob(a,b))