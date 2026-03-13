# Calculate the probability of observing more than 6 heads from 10 fair coin flips using CDF.

import scipy.stats as stats

# Number of trials (coin flips)
n = 10

# Probability of getting heads in 1 flip
prob = 0.5

# We want the probability of getting MORE THAN 6 heads
# First we calculate the probability of getting 6 heads OR LESS using CDF
prob_less_than_6 = stats.binom.cdf(6, n, prob)

# Now substract from 1 to get the probability of getting MORE THAN 6 heads
prob_more_than_6 = 1 - prob_less_than_6

# Print the final answer
print("Probability of getting more than 6 heads from 10 fair coin flips is", prob_more_than_6)