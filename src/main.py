import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/train.csv")

print("Food Delivery Dataset")
print("---------------------")

# First 5 rows
print(df.head())

# Shape
print("\nRows and Columns:")
print(df.shape)

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Duplicate rows
print("\nDuplicate Rows:")
print(df.duplicated().sum())

# Data types
print("\nData Types:")
print(df.dtypes)
"""
"
Core Feature 1:
Displays the available food items and their prices.
"""
# Core Feature 1 - Display Food Menu

food_menu = {
    1: ("Pizza", 250),
    2: ("Burger", 150),
    3: ("Biryani", 200),
    4: ("Fried Rice", 180),
    5: ("Sandwich", 120)
}

print("\n------ FOOD MENU ------")
for item, details in food_menu.items():
    print(f"{item}. {details[0]} - ₹{details[1]}")
