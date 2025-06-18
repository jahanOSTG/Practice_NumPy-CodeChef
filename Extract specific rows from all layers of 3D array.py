import numpy as np

def extract_rows_from_layers(depth, rows, cols, row_indices):
    # Create a 3D array with sequential numbers from 0 to depth*rows*cols - 1
    array_3d = np.arange(depth * rows * cols).reshape(depth, rows, cols)
    
    # Extract the specified rows from all layers
    result = array_3d[:, row_indices, :]
    
    return result

# Take depth of the 3D array as input 
depth = int(input())

# Take number of rows as input
rows = int(input())

# Take number of columns as input
cols = int(input())

# Take row_indices to extract as input
row_indices = list(map(int, input().split()))

# Call the function and print the result
result = extract_rows_from_layers(depth, rows, cols, row_indices)
print(result)
