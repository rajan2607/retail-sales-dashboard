import pandas as pd
import sqlite3

# Load CSV file
df = pd.read_csv("data/sales.csv")

# Create SQLite database
conn = sqlite3.connect("sales.db")

# Write data to SQL table
df.to_sql("sales", conn, if_exists="replace", index=False)

print("Sales database created successfully!")
print(df.head())
