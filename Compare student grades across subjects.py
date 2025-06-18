import numpy as np

# Get the number of students
n = int(input())

# Initialize arrays for Math and Science grades
math_grades = np.array([int(input()) for i in range(n)])
science_grades = np.array([int(input()) for i in range(n)])

# Reshape the arrays to 2D (n x 1)
math_grades = math_grades.reshape(-1, 1)
science_grades = science_grades.reshape(-1, 1)

# Create masks for scores ≥ 80
math_mask = math_grades >= 80
science_mask = science_grades >= 80

# Mask for students who scored 80+ in both subjects
both_subjects_mask = np.logical_and(math_mask, science_mask)

# Mask for students who scored 80+ in at least one subject
either_subject_mask = np.logical_or(math_mask, science_mask)
# Print the results of students who scored 80 or above in both subjects
print(np.where(both_subjects_mask)[0] + 1)  # Adding 1 to convert from 0-based to 1-based indexing

# print the results of students who scored 80 or above in at least one subject
print(np.where(either_subject_mask)[0] + 1)  # Adding 1 to convert from 0-based to 1-based indexing
