import numpy as np

# Array of 20 songs
songs = np.array(['Song A', 'Song B', 'Song C', 'Song D', 'Song E',
                  'Song F', 'Song G', 'Song H', 'Song I', 'Song J',
                  'Song K', 'Song L', 'Song M', 'Song N', 'Song O',
                  'Song P', 'Song Q', 'Song R', 'Song S', 'Song T'])

# Get indices form user
# Create a playlist by selecting songs using their indices
# Hint: Use integer array indexing
user=list(map(int,input().split()))
playlist=songs[user]

# Print the playlist
print(playlist)
