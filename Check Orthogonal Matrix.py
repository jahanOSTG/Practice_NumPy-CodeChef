import numpy as np

# Get the number of equations from user
n = int(input())

A = []
for i in range(n):
    # Enter n coefficients for each equation
    row = list(map(float, input().split()))
    A.append(row)
A = np.array(A)

# Enter n constants for each equation
b = list(map(float, input().split()))
b = np.array(b)

x = x = np.linalg.solve(A, b)# solve the equation
print(x)

