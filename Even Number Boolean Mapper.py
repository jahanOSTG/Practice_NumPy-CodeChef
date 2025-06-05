import numpy as np

def even_number_mapper(numbers):
    # Convert the input list to a NumPy array
    arr = np.array(numbers)
    
    # Create a boolean array where True represents even numbers
    # Your code here
    even_mask=arr % 2 ==0
    return even_mask

# Get input from the user
input_numbers = input().split()
numbers_list = [int(num) for num in input_numbers]

# Call the function and print the result
result = even_number_mapper(numbers_list)
print(result)
