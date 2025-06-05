import numpy as np

start = int(input())
end = int(input())

# Create a NumPy array of odd numbers from start to end
odd_numbers =np.arrange(start,end) # Your code here
odd_numbers=[odd_numbers % 2 != 0]

# Print array of odd numbers
print(odd_numbers)
