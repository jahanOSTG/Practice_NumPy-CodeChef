import numpy as np

# Ask the user for the number of rolls
num_rolls = int(input())

# Create a NumPy array of random dice rolls
dice_rolls = np.random.randint(1, 7, size=num_rolls) # Your code here

# Print the resulting array
print(dice_rolls)
