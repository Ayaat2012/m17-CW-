#Suppose that we expect it to rain 10 times in the next 30 days. 
#The number of times it rains in the next 30 days is “Poisson distributed” with lambda = 10. 
# Calculate the probability of exactly 6 days of rain. 
# Also, calculate the probability of 12-14 days of rain

import scipy.stats as stats

# Average number of rainy days
lamda_value = 10

# Probability of raining EXACTLY 6 days
prob_exactly_6 = stats.poisson.pmf(6, lamda_value)
print("Probability of raining exactly 6 days, is", prob_exactly_6)

# Probability of raining BETWEEN 12 and 14 days
prob_12 = stats.poisson.pmf(12, lamda_value)
prob_13 = stats.poisson.pmf(13, lamda_value)
prob_14 = stats.poisson.pmf(14, lamda_value)
prob_12_to_14 = prob_12 + prob_13 + prob_14
print("\nProbability of raining between 12 and 14 days, is", prob_12_to_14)

# Probability of raining AT MOST 8 days
prob_at_most_8 = stats.poisson.cdf(8, lamda_value)
print("\nProbability of raining at most 8 days, is", prob_at_most_8)

# Probability of raining MORE THAN 15 days
prob_more_than_15 = 1 - stats.poisson.cdf(15, lamda_value)
print("\nProbability of raining more than 15 days, is", prob_more_than_15)