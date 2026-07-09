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
"""
Core Feature 2:
Allows the user to select a food item and add it to the cart.
"""

# Core Feature 2 - Add to Cart

cart = []

try:
    choice = int(input("Enter food item number: "))

    if choice in food_menu:
        cart.append(food_menu[choice])
        print("Item added to cart!")
    else:
        print("Invalid item.")

except ValueError:
    print("Please enter a valid number.")
    
"""
Core Feature 3:
Calculates the total bill amount for the selected food items.
"""
# Core Feature 3 - Total Bill

total = 0

for item in cart:
    total += item[1]

print("Total Bill: ₹", total)
