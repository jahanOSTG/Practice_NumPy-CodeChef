import numpy as np

# Get user input
input_string = input()
numbers = [int(x) for x in input_string.split()]

# Create a NumPy array
arr = np.array(numbers)

# Create a boolean mask for non-negative numbers
# Your code here
positive= arr >=0
result=arr[positive]

# Apply the mask to get only non-negative numbers
# Your code here

# print the non-negative numbers
print( result)
