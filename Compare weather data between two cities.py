import numpy as np

# Get 7 temperatures for City A separated by spaces from input
city_a_temps = list(map(int, input().split()))

# Get 7 temperatures for City B separated by spaces from input
city_b_temps = list(map(int, input().split()))

# Convert lists to NumPy arrays
city_a = np.array(city_a_temps)
city_b = np.array(city_b_temps)

# Calculate the temperature difference
# Your code here

# Print the temperature difference (City A - City B)
temp_difference=np.array(city_a-city_b)

print(temp_difference)
