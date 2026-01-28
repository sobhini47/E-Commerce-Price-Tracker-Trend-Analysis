import pandas as pd

# Load CSV
df = pd.read_csv("ecommerce_data.csv")
print("Original data shape:", df.shape)

# Clean Price: remove ₹ and commas, convert to numeric
df["Price"] = df["Price"].astype(str).str.replace("₹", "", regex=True).str.replace(",", "", regex=True)
df["Price"] = pd.to_numeric(df["Price"], errors="coerce")

# Convert Rating to numeric and fill missing ratings with mean
df["Rating"] = pd.to_numeric(df["Rating"], errors="coerce")
mean_rating = df["Rating"].mean()
df["Rating"] = df["Rating"].fillna(mean_rating)  # avoids FutureWarning

# Remove duplicate products
df.drop_duplicates(subset=["Product Name"], inplace=True)

# Drop rows with missing Price
df.dropna(subset=["Price"], inplace=True)

# Reset index
df.reset_index(drop=True, inplace=True)

# Sort by Rating descending
df.sort_values(by="Rating", ascending=False, inplace=True)

# Save cleaned data
df.to_csv("ecommerce_data_cleaned.csv", index=False)

# Display info & top 5 products
print("\n✅ Cleaned data saved to ecommerce_data_cleaned.csv")
print("Cleaned data shape:", df.shape)
print("\nTop 5 products by Rating:\n")
print(df.head())