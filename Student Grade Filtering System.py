import numpy as np

# Input: Number of students and subjects
n_students = int(input())
n_subjects = int(input())

# Grades input
grades = np.array([list(map(int, input().split())) for _ in range(n_students)])

# Thresholds
high_threshold = 80
low_threshold = 50

# Count how many subjects each student scored > 80
high_scores = (grades > high_threshold).sum(axis=1)

# Count how many subjects each student scored < 50
low_scores = (grades < low_threshold).sum(axis=1)

# Condition: At least 2 high scores and at most 1 low score
mask = (high_scores >= 2) & (low_scores <= 1)

# Get the indices of students satisfying the condition
result = np.where(mask)[0]

# Print result
print(result)
