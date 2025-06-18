import numpy as np

def celsius_to_fahrenheit_grid(celsius_temps):
    # Create a 2D array from the 1D input array
    celsius_2d = celsius_temps.reshape(-1, 1)
    
    # Convert Celsius to Fahrenheit using broadcasting
    # Your code here
    fahrenheit_grid=celsius_2d*(9/5)+32
    return fahrenheit_grid

# Get celsius temperatures separated by spaces from user
celsius_input = input().split()
celsius_temps = np.array([float(temp) for temp in celsius_input])

# Call the function and print the result
result = celsius_to_fahrenheit_grid(celsius_temps)

# Print temperature conversion grid
print(result)
