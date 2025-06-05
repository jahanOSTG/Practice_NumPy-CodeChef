import numpy as np

# Get input from the user and convert it into numpy array of integers
input_list = input().split()
input_array = np.array(input_list, dtype=int)

# Extract every third element
result=input_array[0::3]


print(result)
