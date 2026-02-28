# Additional Rule

# Event A is rolling an even number on a six-sided dice
# and Event B is rolling a number greater than two
# # Find the probability of both events occurring by using the Addition method

even = {2, 4, 6}
greater_than_2 = {3, 4, 5, 6}
total = {1, 2, 3, 4, 5, 6}

prob_a = len(even) / len(total)
prob_b = len(greater_than_2) / len(total)

i = even.intersection(greater_than_2)

prob_i_a_b = len(i) / len(total)

addition = prob_a + prob_b - prob_i_a_b
print(round(addition, 2))