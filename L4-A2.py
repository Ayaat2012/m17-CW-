#Suppose that the following is true (this is shown in the first set of branches in the diagram): 
# - 20 percent of the population has strep throat. 
# - 80 percent of the population does not have strep throat. 
#Now suppose that we test a bunch of people for strep throat. 
#The possible results of these tests are shown in the next set of branches: 
# - If a person has strep throat, 
# there is an 85% chance their test will be positive and a 15% chance it will be negative. 
# - If a person does not have strep throat, 
# there is a 98% chance their test will be negative and a 2% chance it will be positive. 
#From previous experiment, we already know that probability of a positive test result given 
#that the person has strep throat is - 0.85 
# Find out the probability, if someone gets a positive result, what is the probability that they have strep throat?


prob_st = 0.2
prob_st_pos = 0.2 * 0.85
prob_st_neg = 0.8 * 0.02

prob_pos = prob_st_pos + prob_st_neg

prob_pos_given_st = 0.85
prob_result = (prob_st * prob_pos_given_st) / prob_pos

print("Probability of person having strep throat given a positive result :", round(prob_result, 2))