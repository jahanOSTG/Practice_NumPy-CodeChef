import numpy as np

# Get user input for dimensions
depth = int(input())
rows = int(input())
cols = int(input())

# Get user input for array elements
elements = input().split()
elements = [int(x) for x in elements]

# Create a 1D NumPy array
arr=np.array(elements)

# Your code to reshape the 1D array into a 3D array goes here
reshaped_arr=arr.reshape((depth,rows,cols))

# Print the reshaped array
print(reshaped_arr)
