import numpy as np

# Create a NumPy array from user input
input_list = input().split()
input_list = [int(score) for score in input_list]
arr = np.array(input_list)

# Your code to reverse the array using slicing goes here
reversed_arr=arr[::-1]
print(reversed_arr)
