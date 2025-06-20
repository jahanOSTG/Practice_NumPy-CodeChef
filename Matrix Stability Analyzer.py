import numpy as np

def matrix_stability_analyzer(matrix):
    # Calculate eigenvalues
    eigenvalues = np.linalg.eigvals(matrix)
    
    # Check stability
    is_stable = all(np.real(val)<0 for val in eigenvalues)
    
    # Calculate determinant
    determinant =np.linalg.det(matrix) # Your code here
    
    return is_stable, determinant, eigenvalues

# Get matrix size from user
n = int(input())

# Get matrix elements from user
matrix = []
for i in range(n):
    # Enter n elements for each rows separated by space
    row = list(map(float, input().split()))
    matrix.append(row)

# Convert to numpy array
matrix = np.array(matrix)

# Analyze matrix stability
stability, det, eig = matrix_stability_analyzer(matrix)

# Print whether matrix is stable
print('stable' if stability else 'unstable')

# Print determinant
print(det)

# Print eigenvalues
print(eig)
