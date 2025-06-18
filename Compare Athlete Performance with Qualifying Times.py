import numpy as np

# Get athletes' performance times from user
athlete_times = np.array(list(map(float, input().split())))

# Qualifying times
qualifying_times = np.array([10.2, 20.5, 45.0, 13.5, 49.5])

# Compare athlete times with qualifying times
qualified =(qualifying_times>=athlete_times) # Your code here

# Print qualification status of athletes
print(qualified)
