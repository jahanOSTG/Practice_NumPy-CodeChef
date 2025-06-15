import numpy as np

# Function to calculate mean and median temperature
def analyze_temperature(temperatures):
    temp_array = np.array(temperatures)
    
    # Calculate mean temperature
    mean_temp =np.mean(temp_array) # Your code here
    
    # Calculate median temperature
    median_temp = np.median(temp_array)# Your code here
    
    return mean_temp, median_temp

# Get daily temperature data from user
temperatures = list(map(float, input().split()))

# Call the function and print results
mean, median = analyze_temperature(temperatures)

# Print mean temperature
print(f"{mean:.2f}")

# Print median temperature
print(f"{median:.2f}")
