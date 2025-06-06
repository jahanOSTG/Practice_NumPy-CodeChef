import numpy as np

# DNA base pairs
pair1 = np.array(['A', 'T'])
pair2 = np.array(['C', 'G'])

# Get the number of repetitions
n = int(input())

# Your code here to create the repeated DNA sequence

x=np.concatenate((pair1,pair2))
dna_sequence=np.tile(x,n)

# Print the repeated DNA sequence
print(dna_sequence)
