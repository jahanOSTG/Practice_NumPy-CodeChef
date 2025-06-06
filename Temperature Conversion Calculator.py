import numpy as np

def celsius_to_fahrenheit(celsius_temps):
    # Your code here
    fahrenheit_array=(celsius_array * (9/5))+32
    return fahrenheit_array
    # Use array broadcasting to convert Celsius to Fahrenheit
    pass

# Get input celsius temperatures separated by spaces from user
celsius_temps = input().split()
celsius_array = np.array(list(map(float, celsius_temps)))

# Call the function and print the result
fahrenheit_array = celsius_to_fahrenheit(celsius_array)
print(fahrenheit_array)
