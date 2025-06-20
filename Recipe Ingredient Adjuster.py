import numpy as np

# Original recipe quantities for 4 servings
original_recipe = np.array([2, 3, 1, 4, 0.5])

# Get the desired number of servings from the user
desired_servings = int(input())

# Calculate the scaling factor
scaling_factor = desired_servings / 4

# Adjust the recipe quantities
# Your code here
adjusted_recipe=original_recipe*scaling_factor

# Print the adjusted recipe quantities
print(adjusted_recipe)
