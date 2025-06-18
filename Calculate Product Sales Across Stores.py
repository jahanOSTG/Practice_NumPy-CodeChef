import numpy as np

# Sales quantity matrix (4 stores x 3 products)
sales_quantity = np.array([
    [10, 5, 3],
    [8, 6, 4],
    [12, 4, 6],
    [6, 8, 2]
])

# Product price matrix (3 products x 1)
product_price = np.array([[5], [8], [12]])

# find total quantity of each product in all four stores
total_quantity_per_product = np.sum(sales_quantity, axis=0)

# Calculate total sales
total_sales =np.array(total_quantity_per_product*product_price) # Your code here

print("Total sales for each product:")
print(total_sales)
