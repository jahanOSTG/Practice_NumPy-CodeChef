import numpy as np

# Get scores(comma-separated) for Class A from user
class_a_scores = input()
class_a_array = np.array([int(score) for score in class_a_scores.split(',')])

# Get scores(comma-separated) for Class B from user
class_b_scores = input()
class_b_array = np.array([int(score) for score in class_b_scores.split(',')])

# Concatenate the two arrays
combined_scores = np.concatenate((class_a_array,class_b_array)) # Your code here

# Print combined scores
print(combined_scores)

# Print Total number of scores
print(len(combined_scores))

# Print Average score
print(np.mean(combined_scores))
