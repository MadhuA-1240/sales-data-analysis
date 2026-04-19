import pandas as pd
import matplotlib.pyplot as plt

# Sample sales dataset
data = {
    "Product": ["A", "B", "C", "D", "E"],
    "Sales": [500, 700, 300, 900, 650],
    "Region": ["East", "West", "North", "South", "East"]
}

df = pd.DataFrame(data)

print("Sales Data:\n", df)

# Total sales
print("\nTotal Sales:", df["Sales"].sum())

# Average sales
print("Average Sales:", df["Sales"].mean())

# Sales by region
region_sales = df.groupby("Region")["Sales"].sum()
print("\nSales by Region:\n", region_sales)

# Visualization
region_sales.plot(kind="bar", title="Sales by Region")
plt.show()
