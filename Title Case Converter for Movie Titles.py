import numpy as np

# Encoding matrix
encoding_matrix = np.array([[2, 1], [1, 3]])

# Encoded message
encoded_message = np.array([[5, 4], [7, 9]])

# Step 1: Invert the encoding matrix
inv_matrix = np.linalg.inv(encoding_matrix)

# Step 2: Decode the message
decoded_matrix = np.dot(inv_matrix, encoded_message)

# Step 3: Round the results to nearest integers
decoded_matrix = np.round(decoded_matrix).astype(int)

# Step 4: Convert numbers to uppercase letters (A=1, B=2, ..., Z=26)
decoded_chars = []
for row in decoded_matrix:
    for num in row:
        if 1 <= num <= 26:
            decoded_chars.append(chr(num + 64))  # chr(65) = 'A'

# Step 5: Combine letters into message
decoded_message = ''.join(decoded_chars)

# Output
print("Decoded message:", decoded_message)
