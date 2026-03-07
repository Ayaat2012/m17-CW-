# Suppose we flip a fair coin 10 times and count the number of heads. 
# Now, calculate the probability of observing 3 heads. 
# Also, find the probability of observing more than 2 heads from 10 coin flips
import scipy.stats as stats

## Probability of observing 3 heads
x = 3
y = 10
prob_heads = 1/2

prob_1 = stats.binom.pmf(0, y, prob_heads)
print("Probability of observing3 heads :", prob_1)

## Probability of observing more than 2 heads from 10 flips
prob_2 = 1 - stats.binom.pmf(0, y, prob_heads) - stats.binom.pmf(1, y, prob_heads) - stats.binom.pmf(1, y, prob_heads)
print("Probability of observing more than 2 heads from 10 flips :", prob_2)