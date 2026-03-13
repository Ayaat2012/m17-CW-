# Working at a call center where the average number of calls between 9am and 10am is 15 calls, 
# - what is the probability of observing more than 20 calls? 
# Also, find the probability of observing between 17 to 21 calls 
# - when the expected number of calls is 15.

import scipy.stats as stats

# Average number of calls per hour
lambda_value = 15

# Probability of getting MORE THAN 20 calls
prob_more_than_20 = 1 - stats.poisson.cdf(20, lambda_value)
print("Probability of getting more than 20 calls, is", prob_more_than_20)


# Probability of getting calls BETWEEN 17 and 21
prob_17_to_21 = stats.poisson.cdf(21, lambda_value) - stats.poisson.cdf(16, lambda_value)
print("\nProbability of getting calls between 17 and 21, is", prob_17_to_21)


# Probability of getting EXACTLY 10 calls
prob_exactly_10 = stats.poisson.pmf(10, lambda_value)
print("\nProbability of getting exactly 10 calls, is", prob_exactly_10)


# Probability of getting AT MOST 12 calls
prob_at_most_12 = stats.poisson.cdf(12, lambda_value)
print("\nProbability of getting at most 12 calls, is", prob_at_most_12)


# Probability of getting LESS THAN 5 calls
prob_less_than_5 = stats.poisson.cdf(5, lambda_value)
print("\nProbability of getting less than 5 calls, is", prob_less_than_5)