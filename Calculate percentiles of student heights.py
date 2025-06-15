import numpy as np

def calculate_height_percentiles(heights):
    # Convert the list to a NumPy array
    heights_array = np.array(heights)
    
    # Calculate the 25th, 50th, and 75th percentiles
    percentiles = np.percentile(heights_array, [25, 50, 75])
    
    return percentiles

# Get student heights input from user
heights = list(map(int, input().split()))

# Call the function and print the result
result = calculate_height_percentiles(heights)
print(result)
