import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from collections import Counter

# List: Remove duplicates and sort
numbers = [4, 2, 9, 2, 5, 4, 7, 9, 1]
unique_sorted_numbers = sorted(set(numbers))
print("Sorted Unique Numbers:", unique_sorted_numbers)

# Set: Find common elements between two lists
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]
common_elements = set(list1) & set(list2)
print("Common Elements:", common_elements)

# Tuple: Sort student records by grade
students = [("Alfiya", 20, 85), ("Ayman", 21, 92), ("Rafid", 19, 78)]
sorted_students = sorted(students, key=lambda student: student[2], reverse=True)
print("Sorted Students:", sorted_students)

# Dictionary: Count word occurrences in a text
text = "I Am a cse student. In this semester, I am learning python programming."
words = text.lower().replace(".", "").split()
word_count = dict(Counter(words).most_common(3))
print("Word Count:", word_count)

# NumPy#1: 5x5 random matrix and row-wise sums
matrix = np.random.randint(1, 10, (5, 5))
row_sums = matrix.sum(axis=1)
print("Matrix:\n", matrix)
print("Row-wise Sums:", row_sums)

# NumPy#2: Normalize an array of 100 random values between 0 and 1
random_values = np.random.rand(100)
normalized_values = (random_values - random_values.min()) / (random_values.max() - random_values.min())
print("Normalized Values:", normalized_values[:5])

# Pandas#1: Load CSV and compute total revenue per product
# Assuming a CSV file 'sales.csv' with columns: 'Product', 'Quantity', 'Price'
sales_data = pd.read_csv('sales.csv')
sales_data['Revenue'] = sales_data['Quantity'] * sales_data['Price']
revenue_per_product = sales_data.groupby('Product')['Revenue'].sum()
print("Total Revenue Per Product:\n", revenue_per_product)
total_revenue = revenue_per_product.sum()
print("Total Revenue from All Products:", total_revenue)


# Pandas#2: Fill missing values with column-wise means
df = pd.read_csv('data.csv')
df.fillna(df.mean(numeric_only=True), inplace=True)
df.fillna({'Name': 'N/A', 'Email': 'N/A'}, inplace=True)
print("Data after filling missing values:\n", df.head())

# Matplotlib#1: Line graph for temperature variations over a week
days = ["Sat", "Sun", "Mon", "Tue", "Wed", "Thu", "Fri"]
temperatures = [22, 24, 19, 23, 25, 21, 20]
plt.plot(days, temperatures, marker='o', linestyle='-', color='c')
plt.xlabel("Days")
plt.ylabel("Temperature (°C)")
plt.title("Temperature Variations Over a Week")
plt.show()

# Matplotlib#2: Bar chart comparing sales revenue across regions
regions = ["Dhaka", "Chittagong", "Sylhet", "Rajshahi"]
sales = [5000, 7000, 5500, 6500]
plt.bar(regions, sales, color=['red', 'blue', 'green', 'purple'])
plt.xlabel("Regions")
plt.ylabel("Sales Revenue ($)")
plt.title("Sales Revenue Across Different Regions")
plt.show()