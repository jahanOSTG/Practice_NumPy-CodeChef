import numpy as np

# Create a 5x5x5 3D array with random integers from 0 to 99
array_3d = np.random.randint(0, 100, size=(5, 5, 5))

# Get user input for cube dimensions
a = int(input())
b = int(input())
c = int(input())

start_x, start_y, start_z = 1, 1, 1

# Calculate end indices ensuring they don't exceed array bounds
end_x = start_x + a
end_y = start_y + b
end_z = start_z + c

# Extract the cube
extracted_cube = array_3d[start_x:end_x, start_y:end_y, start_z:end_z]

# Print the extracted cube
print(extracted_cube)
