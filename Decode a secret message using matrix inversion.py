import numpy as np

# Encoding matrix
encoding_matrix = np.array([[2, 1], [1, 3]])

# Encoded message (you can change this to test different messages)
encoded_message = np.array([[5, 4], [7, 9]])
# Step 1: Invert the encoding matrix
inv_matrix = np.linalg.inv(encoding_matrix)

# Step 2: Decode the message
decoded_message = np.dot(inv_matrix, encoded_message)
# Print the decoded message
print("Decoded message:")
print(decoded_message)
