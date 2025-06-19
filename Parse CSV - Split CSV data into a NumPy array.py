import numpy as np

def parse_csv(csv_string):
    # Split the csv_string into rows
    rows = csv_string.strip().split('\n')
    
    # Split each row into values and convert to int
    data = [list(map(int, row.split(','))) for row in rows]
    
    # Convert the list of lists to a NumPy array
    result_array = np.array(data)
    
    return result_array

# Test the function
csv_data = """1,2,3
4,5,6
7,8,9"""

result = parse_csv(csv_data)
print(result)

