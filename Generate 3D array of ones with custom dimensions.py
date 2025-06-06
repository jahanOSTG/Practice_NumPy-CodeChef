import numpy as np

def create_3d_ones(depth, rows, columns):
    # Your code here
    return np.ones((depth,rows,columns),dtype=int)
    pass

# Take depth, rows, and columns as input
d, r, c = map(int, input().split())

# Test the function
result = create_3d_ones(d, r, c)

print(result)
