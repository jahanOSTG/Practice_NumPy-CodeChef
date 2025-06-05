import numpy as np

def convert_to_grades(scores):
    # Create a NumPy array from the input list
    score_array = np.array(scores)
    
    # Create an empty string array of the same shape as score_array
    grade_array = np.empty_like(score_array, dtype='U1')
    
    # Your code here to fill grade_array with letter grades
    grade_array[(score_array >= 90) & (score_array <= 100)] = 'A'
    grade_array[(score_array >= 80) & (score_array <= 89)] = 'B'
    grade_array[(score_array >= 70) & (score_array <= 79)] = 'C'
    grade_array[(score_array >= 60) & (score_array <= 69)] = 'D'
    grade_array[score_array < 60] = 'F'

    
    return grade_array

# Get input from user
scores = input().split()
scores = [int(score) for score in scores]

# we can also use map to take input: scores = list(map(int, input().split()))

# Call the function and print the result
result = convert_to_grades(scores)
print(result)
