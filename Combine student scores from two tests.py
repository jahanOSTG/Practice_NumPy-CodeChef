import numpy as np

# Get comma-separated input for test1 scores 
test1_scores = list(map(int, input().split(',')))

# Get comma-separated input for test2 scores
test2_scores = list(map(int, input().split(',')))

# Convert lists to NumPy arrays
arr1 = np.array(test1_scores)
arr2 = np.array(test2_scores)

# Create boolean masks for scores >= 70
mask1 = arr1 >= 70
mask2 = arr2 >= 70

# TODO: Use logical OR to find students who performed well in either test
performed_well_either=np.logical_or(mask1,mask2)
# TODO: Use logical AND to find students who performed well in both tests
performed_well_both=np.logical_and(mask1,mask2)
# Print results of students who performed well in either test
print(performed_well_either)

# Print results of students who performed well in both tests
print(performed_well_both)
