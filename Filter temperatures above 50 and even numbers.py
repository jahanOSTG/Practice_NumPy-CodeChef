import numpy as np

# Get temperature data from user input
temperatures = list(map(int, input().split()))
temp_array = np.array(temperatures)

# Apply filtering: even temperatures > 50
filtered_temps = temp_array[(temp_array > 50) & (temp_array % 2 == 0)]

# Print the result
print(filtered_temps)
