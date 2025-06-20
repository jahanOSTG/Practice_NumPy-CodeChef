import numpy as np

# Get input words from the user
words = input().split()

# Convert the list to a NumPy array
word_array = np.array(words)

# Replace vowels with asterisks
# Your code here
vowels="aeiouAEIOU"
for i in vowels:
    word_array=np.char.replace(word_array,i,'*')

# Print the modified array
print(word_array)
