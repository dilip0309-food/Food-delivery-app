import pandas as pd

# Load dataset
df = pd.read_csv("train.csv")

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
