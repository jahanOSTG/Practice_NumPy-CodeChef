import numpy as np

def calculate_performance_metrics(scores):
    # Your code here
    subject_averages=np.mean(scores,axis=0)
    subject_highest=np.max(scores,axis=0)
    total=scores.size
    pass_=np.sum(scores>=50)
    overall_pass_percentage=(pass_/total)*100
    
    
    return subject_averages, subject_highest, overall_pass_percentage

# Example usage
scores = np.array([
    [75, 80, 65, 90],
    [60, 70, 55, 85],
    [80, 75, 70, 95],
    [45, 60, 75, 70],
    [85, 90, 80, 88]
])

subject_averages, subject_highest, overall_pass_percentage = calculate_performance_metrics(scores)
print("Subject Averages:", subject_averages)
print("Subject Highest Scores:", subject_highest)
print("Overall Pass Percentage:", overall_pass_percentage)
