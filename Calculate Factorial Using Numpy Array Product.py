import numpy as np

def calculate_factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers"
    elif n == 0 or n == 1:
        return 1
    else:
        # Create a NumPy array of integers from 1 to n
        arr = np.arange(1, n+1)
        
        # Calculate the product of all elements in the array
        # Your code here
        factorial=np.prod(arr)
        
        return factorial

# Test the function
n = int(input())
print(calculate_factorial(n))
