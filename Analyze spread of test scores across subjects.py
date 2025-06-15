import numpy as np

def analyze_test_scores(scores):
    # Calculate the mean scores for each subject
    mean_scores = np.mean(scores, axis=0)
    
    # Calculate the variance for each subject
    # Your code here
    variances=np.var(scores,axis=0)
    # Calculate the standard deviation for each subject
    std_deviations=np.std(scores,axis=0)
    # Your code here
    
    return mean_scores, variances, std_deviations

# Get count of students and subjects from user
num_students = int(input())
num_subjects = int(input())

scores = []

# Get scores of students from user 
for i in range(num_students):
    student_scores = list(map(float, input().split()))
    scores.append(student_scores)

scores_array = np.array(scores)

mean_scores, variances, std_deviations = analyze_test_scores(scores_array)

# Print mean scores
print(mean_scores)

# Print variances
print(variances)

# Print standard deviations
print(std_deviations)
