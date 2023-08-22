# Monopoly: https://open.kattis.com/problems/monopol
# Resources: https://www.pdx.edu/learning-center/sites/g/files/znldhr3391/files/2020-07/Probability_Dice.pdf
# Cosme M. Tejeda

# Total number of dice combinations: 36
# Probability for each sum from  2 to 12: 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1
# sum_prob = list(map(lambda i: i / 36, [0, 0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1])) # Method 1
sum_prob = [i / 36 for i in [0, 0, 1, 2, 3, 4, 5, 6, 5, 4, 3, 2, 1]] # Method 2
prob = 0

input()
distances = input().split()

for dist in distances:
    prob += sum_prob[int(dist)]
print(prob)
